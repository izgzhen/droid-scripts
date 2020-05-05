IC3: Installation and Usage
====


Before you can use IC3, you should make sure that you have a Java Runtime Environment version 7 or later installed. To install IC3, download and extract the installation archive (zip, tar.gz, or tar.bz2). It contains the IC3 Jar archive, another archive containing Android libraries, and various database-related files.
Android applications need to be retargeted to Java bytecode before analysis. You can use Dare in order to do so.
IC3 can be launched using:

    % java [JVM options] -jar <path to IC3 Jar> -apkormanifest <path to .apk> \
    -input <path to retargeted application> -cp <path to Android Jar> [IC3 options]

IC3 outputs the list of values it finds for Intents and Intent Filters. You may have to specify a larger heap size for medium to large applications. In order to do so, you need to replace [JVM options] with -Xmx4g (for a 4GB heap).
It is possible to have IC3 store its results into a MySQL database. The schema file is located under the `db` directory. The database should be called `cc` and one of the users who have access to it should have permission to select and insert rows into it. Once the database has been created, from the mysql command prompt you can do the following:

    mysql> use cc
    mysql> source <path to schema file>

In order for IC3 to be able to access the database, you need to set the properties indicated in the `db/cc.properties.template` file. You then have to point IC3 to it by using the following option: `-db <path to cc.properties file>`. If you wish to connect to the database via SSH, you should also set the proper values in the `db/ssh.properties.template` file. You can then point IC3 to it by using option `-ssh <path to ssh.properties file>`.
It is also possible to have IC3 output the results of its analysis to protocol buffers. This allows you to examine results in an easier way than through the database. More importantly, you can easily load IC3 results using code written in Java, Python or C++. In order to output to a protocol buffer, the `-protobuf` option followed by the path to an output directory can be used. In order to output to a binary protocol buffer (which is slightly faster and takes less space), use the `-binary` option. The `-protobuf` option is not compatible with the `-db` option.
Finally, it is possible to have IC3 compute which components a message-sending program location belongs. This is done by specifying the `-computecomponents` flag on the command line.
Please submit any questions or issues to the issue tracker for IC3.
