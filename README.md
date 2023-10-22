<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Project_Big_Data_Mastodon_Data_Analysis_with_Airflow_Hadoop_and_HBase_0"></a>Project Big Data Mastodon Data Analysis with Airflow, Hadoop, and HBase</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Introduction_2"></a>Introduction</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">This project is dedicated to the analysis of data from the Mastodon platform and aims to address various critical needs for the extraction, processing, and analysis of massive data. As a data developer, the mission is to establish an automated pipeline to tackle these complex challenges. This project responds to the necessity of extracting meaningful insights from raw Mastodon data, focusing on user analysis, content analysis, language analysis, media engagement, tags, mentions, and more. To achieve this, several key steps need to be followed, from raw data collection to in-depth analysis of the results. These needs define the framework of this Big Data project and will be detailed in the following sections.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Planning_6"></a>Planning</h2>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/f38055c4-189b-4e8a-9cb5-be758231c2f4">

<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="Requirements_Expression__8"></a>Requirements Expression :</h3>
<ul>
<li class="has-line-data" data-line-start="10" data-line-end="11"><strong>Data Collection:</strong> Use the Mastodon API, store data in HDFS, and model the HDFS Data Lake.</li>
<li class="has-line-data" data-line-start="11" data-line-end="12"><strong>MapReduce Processing:</strong> Mapper and reducer to transform and aggregate data.</li>
<li class="has-line-data" data-line-start="12" data-line-end="13"><strong>MapReduce Job Execution:</strong> Utilize the Hadoop streaming API and monitor through the Hadoop Web interface.</li>
<li class="has-line-data" data-line-start="13" data-line-end="14"><strong>Store Results in HBase:</strong> Design the HBase schema, create tables, and insert data.</li>
<li class="has-line-data" data-line-start="14" data-line-end="15"><strong>Orchestration with Apache Airflow:</strong> Define a DAG, create tasks, and monitor through Airflow.</li>
<li class="has-line-data" data-line-start="15" data-line-end="16"><strong>Results Analysis:</strong> Query data in HBase to extract information about users, content, language, media engagement, tags, and mentions.</li>
<li class="has-line-data" data-line-start="16" data-line-end="17"><strong>Optimization and Monitoring:</strong> Optimize MapReduce scripts, monitor HBase, set up Airflow alerts, and monitor Hadoop.</li>
<li class="has-line-data" data-line-start="17" data-line-end="18"><strong>Update Permissions and Documentation:</strong> Update API tokens, document roles, permissions, and access rules.</li>
<li class="has-line-data" data-line-start="18" data-line-end="19"><strong>Scheduled Developments:</strong> Regularly schedule DAGs to keep data current.</li>
<li class="has-line-data" data-line-start="19" data-line-end="21"><strong>GDPR Compliance:</strong> Document personal data, comply with GDPR regulations.</li>
</ul>
<h2 class="code-line" data-line-start=21 data-line-end=22 ><a id="Environment___21"></a>Environment  :</h2>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="Hadoop_Installation_Script_2"></a>Hadoop Installation Script</h3>
<p class="has-line-data" data-line-start="4" data-line-end="5">This script guides you through the installation of Hadoop on Ubuntu. It covers the installation of Java, Hadoop, SSH configuration, and the necessary environment setup.</p>
<h4 class="code-line" data-line-start=6 data-line-end=7 ><a id="Installing_Java_on_Ubuntu_6"></a>Installing Java on Ubuntu</h4>
<pre><code class="has-line-data" data-line-start="9" data-line-end="13" class="language-bash">sudo apt install default-jre default-jdk -y
java -version
readlink $(<span class="hljs-built_in">which</span> javac)
</code></pre>
<h4 class="code-line" data-line-start=14 data-line-end=15 ><a id="Create_a_user_for_Hadoop_and_configure_SSH_14"></a>Create a user for Hadoop and configure SSH</h4>
<pre><code class="has-line-data" data-line-start="17" data-line-end="26" class="language-bash">sudo adduser hadoop
sudo usermod <span class="hljs-operator">-a</span>G sudo hadoop
sudo su - hadoop
sudo apt install openssh-server openssh-client -y
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub &gt;&gt; ~/.ssh/authorized_keys 
sudo chmod <span class="hljs-number">640</span> ~/.ssh/authorized_keys
ssh localhost
</code></pre>
<h4 class="code-line" data-line-start=27 data-line-end=28 ><a id="Download_and_install_Apache_Hadoop_on_Ubuntu_27"></a>Download and install Apache Hadoop on Ubuntu</h4>
<pre><code class="has-line-data" data-line-start="30" data-line-end="36" class="language-bash">wget https://dlcdn.apache.org/hadoop/common/hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>/hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>.tar.gz
tar -xvzf hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>.tar.gz
sudo mv hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span> /usr/<span class="hljs-built_in">local</span>/hadoop
sudo mkdir /usr/<span class="hljs-built_in">local</span>/hadoop/logs
sudo chown -R hadoop:hadoop /usr/<span class="hljs-built_in">local</span>/hadoop
</code></pre>
<h4 class="code-line" data-line-start=37 data-line-end=38 ><a id="Configure_Hadoop_on_Ubuntu_37"></a>Configure Hadoop on Ubuntu</h4>
<pre><code class="has-line-data" data-line-start="40" data-line-end="42" class="language-bash">sudo nano ~/.bashrc
</code></pre>
<p class="has-line-data" data-line-start="43" data-line-end="44">Add the following lines to <code>~/.bashrc</code>:</p>
<pre><code class="has-line-data" data-line-start="46" data-line-end="56" class="language-bash"><span class="hljs-built_in">export</span> HADOOP_HOME=/usr/<span class="hljs-built_in">local</span>/hadoop
<span class="hljs-built_in">export</span> HADOOP_INSTALL=<span class="hljs-variable">$HADOOP_HOME</span>
<span class="hljs-built_in">export</span> HADOOP_MAPRED_HOME=<span class="hljs-variable">$HADOOP_HOME</span>
<span class="hljs-built_in">export</span> HADOOP_COMMON_HOME=<span class="hljs-variable">$HADOOP_HOME</span>
<span class="hljs-built_in">export</span> HADOOP_HDFS_HOME=<span class="hljs-variable">$HADOOP_HOME</span>
<span class="hljs-built_in">export</span> YARN_HOME=<span class="hljs-variable">$HADOOP_HOME</span>
<span class="hljs-built_in">export</span> HADOOP_COMMON_LIB_NATIVE_DIR=<span class="hljs-variable">$HADOOP_HOME</span>/lib/native
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$PATH</span>:<span class="hljs-variable">$HADOOP_HOME</span>/sbin:<span class="hljs-variable">$HADOOP_HOME</span>/bin
<span class="hljs-built_in">export</span> HADOOP_OPTS=<span class="hljs-string">"-Djava.library.path=<span class="hljs-variable">$HADOOP_HOME</span>/lib/native"</span>
</code></pre>
<p class="has-line-data" data-line-start="57" data-line-end="58">Apply the changes:</p>
<pre><code class="has-line-data" data-line-start="60" data-line-end="62" class="language-bash"><span class="hljs-built_in">source</span> ~/.bashrc
</code></pre>
<h4 class="code-line" data-line-start=63 data-line-end=64 ><a id="Configure_java_environment_variables_63"></a>Configure java environment variables</h4>
<pre><code class="has-line-data" data-line-start="66" data-line-end="68" class="language-bash">sudo nano <span class="hljs-variable">$HADOOP_HOME</span>/etc/hadoop/hadoop-env.sh
</code></pre>
<p class="has-line-data" data-line-start="69" data-line-end="70">Add the following lines to <code>hadoop-env.sh</code>:</p>
<pre><code class="has-line-data" data-line-start="72" data-line-end="75" class="language-bash"><span class="hljs-built_in">export</span> JAVA_HOME=/usr/lib/jvm/java-<span class="hljs-number">11</span>-openjdk-amd64
<span class="hljs-built_in">export</span> HADOOP_CLASSPATH+=<span class="hljs-string">" <span class="hljs-variable">$HADOOP_HOME</span>/lib/*.jar"</span>
</code></pre>
<p class="has-line-data" data-line-start="76" data-line-end="77">Edit the <code>hadoop-env.sh</code> file:</p>
<pre><code class="has-line-data" data-line-start="79" data-line-end="84" class="language-bash"><span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/hadoop/lib
sudo wget https://jcenter.bintray.com/javax/activation/javax.activation-api/<span class="hljs-number">1.2</span>.<span class="hljs-number">0</span>/javax.activation-api-<span class="hljs-number">1.2</span>.<span class="hljs-number">0</span>.jar
hadoop version
<span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/hadoop/lib
</code></pre>
<h4 class="code-line" data-line-start=85 data-line-end=86 ><a id="Edit_the_coresitexml_file_85"></a>Edit the core-site.xml file</h4>
<pre><code class="has-line-data" data-line-start="88" data-line-end="90" class="language-bash">sudo nano <span class="hljs-variable">$HADOOP_HOME</span>/etc/hadoop/core-site.xml
</code></pre>
<p class="has-line-data" data-line-start="91" data-line-end="92">Add the following configuration to <code>core-site.xml</code>:</p>
<pre><code class="has-line-data" data-line-start="94" data-line-end="100" class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>fs.default.name<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>hdfs://localhost:9000<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">description</span>&gt;</span>The default file system URI<span class="hljs-tag">&lt;/<span class="hljs-title">description</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>
</code></pre>
<p class="has-line-data" data-line-start="101" data-line-end="102">Create directories for HDFS:</p>
<pre><code class="has-line-data" data-line-start="104" data-line-end="107" class="language-bash">sudo mkdir -p /home/hadoop/hdfs/{namenode,datanode}
sudo chown -R hadoop:hadoop /home/hadoop/hdfs
</code></pre>
<h4 class="code-line" data-line-start=108 data-line-end=109 ><a id="Edit_the_hdfssitexml_configuration_file_108"></a>Edit the hdfs-site.xml configuration file</h4>
<pre><code class="has-line-data" data-line-start="111" data-line-end="113" class="language-bash">sudo nano <span class="hljs-variable">$HADOOP_HOME</span>/etc/hadoop/hdfs-site.xml
</code></pre>
<p class="has-line-data" data-line-start="114" data-line-end="115">Add the following configuration to <code>hdfs-site.xml</code>:</p>
<pre><code class="has-line-data" data-line-start="117" data-line-end="132" class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>dfs.replication<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>1<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>

<span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>dfs.name.dir<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>file:///home/hadoop/hdfs/namenode<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>

<span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>dfs.data.dir<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>file:///home/hadoop/hdfs/datanode<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>
</code></pre>
<h4 class="code-line" data-line-start=133 data-line-end=134 ><a id="Edit_the_mapredsitexml_file_133"></a>Edit the mapred-site.xml file</h4>
<pre><code class="has-line-data" data-line-start="136" data-line-end="138" class="language-bash">sudo nano <span class="hljs-variable">$HADOOP_HOME</span>/etc/hadoop/mapred-site.xml
</code></pre>
<p class="has-line-data" data-line-start="139" data-line-end="140">Add the following configuration to <code>mapred-site.xml</code>:</p>
<pre><code class="has-line-data" data-line-start="142" data-line-end="147" class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>mapreduce.framework.name<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>yarn<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>
</code></pre>
<h4 class="code-line" data-line-start=148 data-line-end=149 ><a id="Edit_the_yarnsitexml_file_148"></a>Edit the yarn-site.xml file</h4>
<pre><code class="has-line-data" data-line-start="151" data-line-end="153" class="language-bash">sudo nano <span class="hljs-variable">$HADOOP_HOME</span>/etc/hadoop/yarn-site.xml
</code></pre>
<p class="has-line-data" data-line-start="154" data-line-end="155">Add the following configuration to <code>yarn-site.xml</code>:</p>
<pre><code class="has-line-data" data-line-start="157" data-line-end="162" class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>yarn.nodemanager.aux-services<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>mapreduce_shuffle<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>
</code></pre>
<h4 class="code-line" data-line-start=163 data-line-end=164 ><a id="Start_the_Hadoop_cluster_163"></a>Start the Hadoop cluster</h4>
<pre><code class="has-line-data" data-line-start="166" data-line-end="171" class="language-bash">hdfs namenode -format
start-dfs.sh
start-yarn.sh
jps
</code></pre>

<img width="540" alt="jps" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/68c88037-1c12-4e73-a7d8-43b7cbd95160">

<h4 class="code-line" data-line-start=172 data-line-end=173 ><a id="Access_the_Hadoop_web_interface_172"></a>Access the Hadoop web interface</h4>
<p class="has-line-data" data-line-start="174" data-line-end="175">Open your web browser and visit:</p>
<pre><code class="has-line-data" data-line-start="177" data-line-end="179" class="language-plaintext">http://server-IP:9870
</code></pre>
<p class="has-line-data" data-line-start="180" data-line-end="181">Replace <code>server-IP</code> with your server’s IP address.</p>

<img width="540" alt="jps" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/80fde465-3a61-42b7-8374-7ebb5040345e">

<h3 class="code-line" data-line-start=25 data-line-end=26 ><a id="HBase_Installation_25"></a>HBase Installation</h3>
<ol>
<li class="has-line-data" data-line-start="27" data-line-end="33">
<p class="has-line-data" data-line-start="27" data-line-end="28"><strong>Download HBase</strong>:</p>
<pre><code class="has-line-data" data-line-start="30" data-line-end="32" class="language-bash">wget http://www.interior-dsgn.com/apache/hbase/stable/hbase-<span class="hljs-number">2.5</span>.<span class="hljs-number">5</span>-bin.tar.gz
</code></pre>
</li>
<li class="has-line-data" data-line-start="33" data-line-end="39">
<p class="has-line-data" data-line-start="33" data-line-end="34"><strong>Extract the downloaded file</strong>:</p>
<pre><code class="has-line-data" data-line-start="36" data-line-end="38" class="language-bash">tar -zxvf hbase-<span class="hljs-number">2.5</span>.<span class="hljs-number">5</span>-bin.tar.gz
</code></pre>
</li>
<li class="has-line-data" data-line-start="39" data-line-end="45">
<p class="has-line-data" data-line-start="39" data-line-end="40"><strong>Move the HBase folder to /usr/local/HBase</strong>:</p>
<pre><code class="has-line-data" data-line-start="42" data-line-end="44" class="language-bash">sudo mv hbase /usr/<span class="hljs-built_in">local</span>/Hbase
</code></pre>
</li>
<li class="has-line-data" data-line-start="45" data-line-end="51">
<p class="has-line-data" data-line-start="45" data-line-end="46"><strong>Access the HBase configuration directory</strong>:</p>
<pre><code class="has-line-data" data-line-start="48" data-line-end="50" class="language-bash"><span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/Hbase/conf
</code></pre>
</li>
<li class="has-line-data" data-line-start="51" data-line-end="88">
<p class="has-line-data" data-line-start="51" data-line-end="52"><strong>HBase Configuration</strong>:</p>
<ul>
<li class="has-line-data" data-line-start="53" data-line-end="66">
<p class="has-line-data" data-line-start="53" data-line-end="54">Edit the <code>hbase-env.sh</code> file:</p>
<pre><code class="has-line-data" data-line-start="56" data-line-end="58" class="language-bash">gedit hbase-env.sh
</code></pre>
<p class="has-line-data" data-line-start="59" data-line-end="60">Add the following lines to set the Java directory and Hadoop classpath:</p>
<pre><code class="has-line-data" data-line-start="62" data-line-end="65" class="language-bash"><span class="hljs-built_in">export</span> JAVA_HOME=/usr/lib/jvm/java-<span class="hljs-number">11</span>-openjdk-amd64
<span class="hljs-built_in">export</span> HADOOP_CLASSPATH+=<span class="hljs-string">" <span class="hljs-variable">$HADOOP_HOME</span>/lib/*.jar"</span>
</code></pre>
</li>
<li class="has-line-data" data-line-start="66" data-line-end="88">
<p class="has-line-data" data-line-start="66" data-line-end="67">Edit the <code>hbase-site.xml</code> file:</p>
<pre><code class="has-line-data" data-line-start="69" data-line-end="71" class="language-bash">gedit hbase-site.xml
</code></pre>
<p class="has-line-data" data-line-start="72" data-line-end="73">Add HBase configuration with the root directory path and ZooKeeper data directory:</p>
<pre><code class="has-line-data" data-line-start="75" data-line-end="87" class="language-xml"><span class="hljs-tag">&lt;<span class="hljs-title">configuration</span>&gt;</span>
  <span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>hbase.rootdir<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>file:/home/hadoop/HBase/HFiles<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
  <span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>

  <span class="hljs-tag">&lt;<span class="hljs-title">property</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">name</span>&gt;</span>hbase.zookeeper.property.dataDir<span class="hljs-tag">&lt;/<span class="hljs-title">name</span>&gt;</span>
    <span class="hljs-tag">&lt;<span class="hljs-title">value</span>&gt;</span>/home/hadoop/zookeeper<span class="hljs-tag">&lt;/<span class="hljs-title">value</span>&gt;</span>
  <span class="hljs-tag">&lt;/<span class="hljs-title">property</span>&gt;</span>
<span class="hljs-tag">&lt;/<span class="hljs-title">configuration</span>&gt;</span>
</code></pre>
</li>
</ul>
</li>
<li class="has-line-data" data-line-start="88" data-line-end="109">
<p class="has-line-data" data-line-start="88" data-line-end="89"><strong>Environment Configuration</strong>:</p>
<ul>
<li class="has-line-data" data-line-start="90" data-line-end="103">
<p class="has-line-data" data-line-start="90" data-line-end="91">Edit the <code>~/.profile</code> file:</p>
<pre><code class="has-line-data" data-line-start="93" data-line-end="95" class="language-bash">sudo gedit ~/.profile
</code></pre>
<p class="has-line-data" data-line-start="96" data-line-end="97">Add these lines to set the <code>HBASE_HOME</code> variable and update the PATH:</p>
<pre><code class="has-line-data" data-line-start="99" data-line-end="102" class="language-bash"><span class="hljs-built_in">export</span> HBASE_HOME=/usr/<span class="hljs-built_in">local</span>/Hbase
<span class="hljs-built_in">export</span> PATH=<span class="hljs-variable">$PATH</span>:<span class="hljs-variable">$HBASE_HOME</span>/bin
</code></pre>
</li>
<li class="has-line-data" data-line-start="103" data-line-end="109">
<p class="has-line-data" data-line-start="103" data-line-end="104">Load the <code>~/.profile</code> file to apply the changes:</p>
<pre><code class="has-line-data" data-line-start="106" data-line-end="108" class="language-bash"><span class="hljs-built_in">source</span> ~/.profile
</code></pre>
</li>
</ul>
</li>
<li class="has-line-data" data-line-start="109" data-line-end="117">
<p class="has-line-data" data-line-start="109" data-line-end="110"><strong>Start HBase</strong>:</p>
<p class="has-line-data" data-line-start="111" data-line-end="112">Launch HBase:</p>
<pre><code class="has-line-data" data-line-start="114" data-line-end="116" class="language-bash">/usr/<span class="hljs-built_in">local</span>/Hbase/bin/start-hbase.sh
</code></pre>
</li>
</ol>

<img width="540" alt="jps" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/1f1f1a5a-b453-44aa-b152-945fa5fbcae0">

<h3 class="code-line" data-line-start=117 data-line-end=118 ><a id="Airflow_Installation__117"></a>Airflow Installation :</h3>
<a href="https://medium.com/international-school-of-ai-data-science/setting-up-apache-airflow-in-ubuntu-324cfcee1427">Apache airflow installation guide</a>
<h2 class="code-line" data-line-start=119 data-line-end=120 ><a id="Data_Collection_119"></a>Data Collection</h2>

To obtain data from the Mastodon platform, I employ a Python script that interacts with the platform's API. The data is retrieved in JSON format, with each object presented on a separate line, a format optimized for preprocessing prior to MapReduce processing.

To execute my code, I use the following command in the terminal:

```bash
python3 get_data.py
```
<img width="540" alt="jps" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/93f0518b-2cfb-4259-8799-d65b3441fed1">

<h2 class="code-line" data-line-start=121 data-line-end=122 ><a id="MapReduce_Processing_121"></a>MapReduce Processing</h2>
<h2 class="code-line" data-line-start=123 data-line-end=124 ><a id="Data_Storage_with_HBa_123"></a>Data Storage with HBas</h2>
