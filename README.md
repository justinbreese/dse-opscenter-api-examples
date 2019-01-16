# dse-opscenter-api-examples
Working with the DataStax OpsCenter API is actually really simple. The location of the API documentation can be found here: https://docs.datastax.com/en/opscenter/6.1/api/docs/index.html

Likewise, I have also created some quick examples that you can use here.

# enable-nodesync.py
This is a quick example on how to enable nodesync on specific keyspaces and/or tables.

* Nodesync is a new feature that can be found in DataStax Enterprise 6.0 and newer.
* It helps alleviate the operation burden of having to manage `nodetool repair` and `nodetool rebuild` throughout your cluster.
* It makes sure that these type of anti-entropy operations are consisently happening in the background. The impact to your cluster performance that has nodesync enabled is very minimal.
* By default, nodesync is not enabled (currently) and you have to enable it per each table

In the example, I list out a group of tables to enable nodesync on. You should see the format: `OpsCenter.*`
* That is enabling nodesync on the entire `OpsCenter` keyspace due to the use of `.*`
* If I wanted to enable nodesync on only a specific table named `foo` within the `OpsCenter` keyspace, then it would look like `OpsCenter.foo`

# update-keyspace.py
This is a quick example on how to update the `strategy_class` for a given keyspace
* In production you only ever want to use `NetworkTopologyStrategy`
* Also, you may want to add another data center
* This example makes both of these scenarios very killrvideo_video_recommendations_system

In the example, I have created an array of keyspaces that I want to all be updated. You will notice `"strategy_options": {"onprem" : "3", "AWS" : "3", "Azure" : "3", "GCP" : "3"}`
* I want to have the keyspaces updated to be on four data centers in total, their names are: onprem, AWS, Azure, and GCP
* I want three replicas of the data in each of the four data opscenter_session
* The code will iterate through the `keyspaces` array and update each keyspace as described above

# the end
There you go! Some quick and dirty API examples. For some more advanced examples, checkout one of my other repos which uses the OpsCenter API to setup a multi-cloud DSE cluster: https://github.com/justinbreese/dse-multi-cloud-demo/setup.py
