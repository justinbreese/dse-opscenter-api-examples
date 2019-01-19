# dse-opscenter-api-examples
Working with the DataStax OpsCenter LCM (Lifecycle Manager) API is actually really simple. The location of the LCM API documentation can be found here: https://docs.datastax.com/en/opscenter/6.7/api/docs/lcm_overview.html

Likewise, I have also created some quick examples that you can use here.

# easiest API call
To do the easiest API call, go to http://IP-address-of-OpsCenter:8888/api/v2/lcm/datacenters
![alt text](https://raw.githubusercontent.com/justinbreese/dse-opscenter-api-examples/master/results.jpg)
* You will notice that this will output a ton of stuff on the datacenters within your cluster
* Congrats, you just did your first API call! This was basically a `GET` request into LCM via the API

# Start to finish: create a cluster
Let's do all of the steps necessary to create a running cluster by only using the API. There is a specific order of operations that we need to do in order to setup a cluster. They are:
* Create a repo
* Create the credentials
* Create a configuration profile
* Create a cluster
* Assign a datacenter to the cluster
* Assign nodes to the datacenter
* Run an install job
* Listen to the install job status (optional)

Follow along as we step through this journey!

## Create your infrastructure
* Create your single OpsCenter node by looking at this link:https://docs.datastax.com/en/opscenter/6.1/opsc/install/opscInstallDeb_t.html or use Docker!
* Make sure that OpsCenter is up and running: `sudo service opscenterd status`
* Create at least one VM that will act as your cluster. Of course you can have as many VMs as you wish here; to represent multiple datacenters, etc.

## create-repo.py
Create a repo that you want the nodes to download DSE from. You can pass your DataStax Academy credentials for this example into the code.
* Be sure to change out the following variables for your environment: `server_ip`, `username`, `password`, and `repo_desc`
* Output: the `repository_id` is outputted by this script, you will need it for future steps!

## create-credentials.py
In order for LCM to interact with the VMs, you will need to give LCM the proper credentials (e.g. SSH, username, password, etc.) to do so
* Be sure to change out the following variables for your environment: `server_ip`, `creds_name`, `username`, and `privateKey`
* Output: the `machine_credential_id` is outputted by this script, you will need it for future steps!

## create-config_profile.py
Do you want to stop editing YAML files? If so, you need to learn how to use configuration profiles
* Configuration profiles a group of defined settings that you can assign to a given cluster, DCs, and/or nodes
* Instead of modifying individual YAML files (dse.yaml, cassandra.yaml, etc.), you can create a single configuration profile and assign it to many nodes, DCs, or clusters
* Be sure to change out the following variables for your environment: `server_ip` and `cluster_name`
* You can specify further configurations that you wish to make to the `cassandra.yaml` and `dse.yaml` JSON properties
* Output: the `cluster_profile_id` is outputted by this script, you will need it for future steps!

## create-cluster.py
Now we can start defining the cluster. To do that, you'll need to bring in the IDs from the previous steps (e.g. `repository_id`, `machine_credential_id`, and `cluster_profile_id`)
* Be sure to change out the following variables for your environment: `server_ip`, `cluster_name`, `repository_id`, `machine_credential_id`, `cassandra_default_password`, and `cluster_profile_id`
* Output: the `cluster_id` is outputted by this script, you will need it for future steps!

## create-datacenter.py
Now that the cluster has been setup, you now have to  at least one datacenter.
* You'll need the `cluster_id` from the previous step
* Be sure to change out the following variables for your environment: `server_ip`, `data_center`, and `cluster_id`
* Output: the `dc_id` that you will use in the next step

## create-nodes.py
In this step, we will assign the node(s) to the appropriate datacenter.
* You'll need the `dc_id` from the previous step
* Be sure to change out the following variables for your environment: `server_ip`, `dc_id`, `node_name`, `private_ip`, and ` node_ip`

## run-job.py
Now that you have configured the cluster, datacenter, and node(s), you have to run a job in order to install everything.
* You'll need the cluster_id from the `create-cluster.py` script
* Be sure to modify the `server_ip`, `job-type`, `resource_id` and the `scope` as needed for the job that you are trying to do.
* Output: the `job_id` that you will use in the next step (optional)

## job-listener.py
Within OpsCenter LCM, you submit a job, but you want to see if it is finished or if it failed. That is what this code does.
* Fill out the `server_ip` and `job_id` variables for what you are listening for

# Bonus Section: but wait, there's more!
You have now created a cluster from scratch with the API, congrats! If you choose, here are some bonus examples.

## enable-nodesync.py
This is a quick example on how to enable nodesync on specific keyspaces and/or tables.
* Nodesync is a new feature that can be found in DataStax Enterprise 6.0 and newer.
* It helps alleviate the operation burden of having to manage `nodetool repair` and `nodetool rebuild` throughout your cluster.
* It makes sure that these type of anti-entropy operations are consisently happening in the background. The impact to your cluster performance that has nodesync enabled is very minimal.
* By default, nodesync is not enabled (currently) and you have to enable it per each table

In the example, I list out a group of tables to enable nodesync on. You should see the format: `OpsCenter.*`
* That is enabling nodesync on the entire `OpsCenter` keyspace due to the use of `.*`
* If I wanted to enable nodesync on only a specific table named `foo` within the `OpsCenter` keyspace, then it would look like `OpsCenter.foo`

## update-keyspace.py
This is a quick example on how to update the `strategy_class` for a given keyspace
* In production you only ever want to use `NetworkTopologyStrategy`
* Also, you may want to add another datacenter and do less that what I have listed; fit it for your use
* In the example, I have created an array of keyspaces that I want to all be updated. You will notice `"strategy_options": {"onprem" : "3", "AWS" : "3", "Azure" : "3", "GCP" : "3"}`
* I want to have the keyspaces updated to be on four datacenters in total, their names are: onprem, AWS, Azure, and GCP
* I want three replicas of the data in each of the four data opscenter_session
* The code will iterate through the `keyspaces` array and update each keyspace as described above

# the end
There you go! Some quick and dirty API examples. For some more advanced examples, checkout one of my other repos which uses the OpsCenter API to setup a multi-cloud DSE cluster: https://github.com/justinbreese/dse-multi-cloud-demo/setup.py

Full reference to the LCM API can be found here: https://docs.datastax.com/en/opscenter/6.7/api/docs/lcm_overview.html
