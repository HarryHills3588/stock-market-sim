# Getting Started
1. Create Maven project structure
```bash
mvn archetype:generate \
-DarchetypeGroupId=org.apache.kafka \
-DarchetypeArtifactId=streams-quickstart-java \
-DarchetypeVersion=4.0.0 \
-DgroupId=stockmarketsim \
-DartifactId=stock-sim-streams \
-Dversion=0.1 \
-Dpackage=stocksim.streams
```