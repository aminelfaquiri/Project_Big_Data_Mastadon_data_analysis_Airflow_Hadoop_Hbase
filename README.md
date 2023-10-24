<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Project_Big_Data_Mastodon_Data_Analysis_with_Airflow_Hadoop_and_HBase_0"></a>Project Big Data Mastodon Data Analysis with Airflow, Hadoop, and HBase</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Introduction_2"></a>Introduction</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">This project is dedicated to the analysis of data from the Mastodon platform and aims to address various critical needs for the extraction, processing, and analysis of massive data. As a data developer, the mission is to establish an automated pipeline to tackle these complex challenges. This project responds to the necessity of extracting meaningful insights from raw Mastodon data, focusing on user analysis, content analysis, language analysis, media engagement, tags, mentions, and more. To achieve this, several key steps need to be followed, from raw data collection to in-depth analysis of the results. These needs define the framework of this Big Data project and will be detailed in the following sections.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Planning_6"></a>Planning</h2>
<img width="616" alt="Capture d'écran 2023-10-24 225520" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/a7970b98-6250-4594-a2ac-2dd08f2c89a2">

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
<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="Requirements_Expression__8"></a>RGBD :</h3>
Ensuring compliance with the General Data Protection Regulation (GDPR) is paramount when handling personal data within the Mastodon data pipeline. This document outlines the key steps taken to adhere to GDPR regulations, demonstrating our commitment to safeguarding personal data and upholding the privacy rights of individuals.

### Key Steps for GDPR Compliance

1. **Data Anonymization:**

   Personal information plays a critical role in GDPR compliance. To meet GDPR requirements, any personal data that is irrelevant to the analysis is either deleted or hashed before processing. This procedure ensures that sensitive personal information remains protected throughout the data pipeline.

2. **Data Minimization:**

   Only the necessary data required for analysis is retained, while any extraneous or irrelevant information is discarded to minimize data exposure and mitigate potential privacy risks.

3. **Security Measures:**

   Our data pipeline employs robust security measures to safeguard data. Both HDFS and HBase storage systems are secured to prevent unauthorized access. Access controls, encryption, and authentication mechanisms are implemented to protect data at rest, ensuring comprehensive data security.

4. **Data Lake Management:**

   To reduce data retention risks, a stringent policy is in place to delete data from the data lake once it has been processed. This practice aligns data retention strictly with the purposes of data processing as specified in the GDPR.

5. **Data Protection Impact Assessment (DPIA):**

   A DPIA is conducted to identify and mitigate potential privacy risks within the data pipeline. This assessment assists in making informed decisions regarding data processing practices and safeguards.

6. **Consent Management:**

   Where applicable, data processing activities are conducted only after obtaining explicit consent from data subjects, as required by GDPR. Consent records are diligently maintained and managed.

7. **Data Subject Rights:**

   Mechanisms are established to accommodate data subject rights as defined by GDPR. This includes providing data subjects with the ability to access, correct, or delete their personal data upon request.

8. **Documentation and Compliance Records:**

   Detailed documentation of data processing activities, safeguards, and compliance measures is consistently maintained. This documentation ensures transparency and accountability in the event of regulatory inquiries.

9. **Regular Auditing and Compliance Checks:**

   Regular audits are conducted to verify the consistent adherence to GDPR compliance measures throughout the data pipeline. This includes ensuring that the pipeline conforms to any changes or updates in GDPR regulations.

10. **Data Breach Response:**

    A well-defined protocol is established to promptly respond to any data breaches in accordance with GDPR requirements. Data subjects and supervisory authorities are notified as required.

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
<img width="680" alt="airflow" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/52e57633-02bc-41d9-9e9f-7b9e1cfaa437">


<h2 class="code-line" data-line-start=119 data-line-end=120 ><a id="Data_Collection_119"></a>Data Collection</h2>

To collect data from the Mastodon platform, I utilize a Python script that communicates with the platform's API. The data is fetched in JSON format, with each object structured on a single line. This format is ideal for preprocessing before undergoing MapReduce processing, and the JSON data is stored in HDFS.

To execute my code, I use the following command in the terminal:

```bash
python3 get_data.py
```
<p class="has-line-data" data-line-start="0" data-line-end="1">The data is retrieved in JSON format and follows the structure shown below:</p>
<img width="540" alt="jps" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/d846f50e-8a60-4bf2-88c9-6c6fe8c7b7ae">
<img width="540" alt="jps" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/a1dcdeb1-7b70-4e05-9d3a-e7516cdf07d4">

<h2 class="code-line" data-line-start=121 data-line-end=122 ><a id="MapReduce_Processing_121"></a>MapReduce Processing</h2>
<p class="has-line-data" data-line-start="0" data-line-end="1">In this step, I will create MapReduce jobs to process my data, extracting key-value pairs for subsequent analysis, and storing the results in HBase tables. Each MapReduce job is responsible for processing and transforming the data, generating key-value pairs, and then saving the processed data into HBase tables. Each specific analysis task is associated with its own set of mapper and reducer scripts</p>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="Number_of_Subscribers_2"></a>user followors,Engagement Rate,User Growth</h3>
<ul>
<li class="has-line-data" data-line-start="4" data-line-end="10"><strong>MapperReducer:</strong><pre><code class="has-line-data" data-line-start="6" data-line-end="9" class="language-python">utilisateure_mapper.py
utilisateure_reducer.py
</code></pre>

</li>
</ul>
<h3 class="code-line" data-line-start=26 data-line-end=27 ><a id="External_Websites_26"></a>External Websites</h3>
<ul>
<li class="has-line-data" data-line-start="28" data-line-end="34"><strong>MapperReducer:</strong><pre><code class="has-line-data" data-line-start="30" data-line-end="33" class="language-python">external_sites_mapper.py
external_sites_reducer.py
</code></pre>  
</li>
</ul>
<h3 class="code-line" data-line-start=34 data-line-end=35 ><a id="Post_Languages_34"></a>Post Languages</h3>
<ul>
<li class="has-line-data" data-line-start="36" data-line-end="42"><strong>MapperReducer:</strong><pre><code class="has-line-data" data-line-start="38" data-line-end="41" class="language-python">analyse_langue_mapper.py
analyse_langue_reducer.py
</code></pre>
</li>
</ul>
<h3 class="code-line" data-line-start=42 data-line-end=43 ><a id="Multimedia_Attachments_42"></a>Multimedia Attachments</h3>
<ul>
<li class="has-line-data" data-line-start="44" data-line-end="50"><strong>MapperReducer:</strong><pre><code class="has-line-data" data-line-start="46" data-line-end="49" class="language-python">attachments_mapper.py
attachments_reducer.py
</code></pre>
</li>
</ul>
<h3 class="code-line" data-line-start=50 data-line-end=51 ><a id="Tags_and_Mentions_50"></a>Tags and Mentions</h3>
<ul>
<li class="has-line-data" data-line-start="52" data-line-end="57"><strong>MapperReducer:</strong><pre><code class="has-line-data" data-line-start="54" data-line-end="57" class="language-python">tag_user_mapper.py
tag_user_reducer.py
</code></pre>

</li>
</ul>
<p class="has-line-data" data-line-start="57" data-line-end="58">All these MapReduce scripts are located in the MapReduce folder.</p>
<h2 class="code-line" data-line-start=123 data-line-end=124 ><a id="Data_Storage_with_HBa_123"></a>Data Storage with HBase</h2>

<h3>Step 1: HBase Table Design and Data Loading</h3>

<p>In this phase, I'll design and create all the necessary HBase tables and populate them with data using MapReduce processes. To create the HBase tables, I'll use a Python script called <code>Tablecreator.py</code>.</p>
<b>use hbase shell to show my table :</b>

<code>hbase shell</code>

<img width="540" alt="Capture d'écran 2023-10-20 222858" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/8b998c13-3df9-4b4a-94d8-e8f28c05870e">
<h3>The HBase Tables schema :</h3>

<h4>user :</h4>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="">

<h4>Content language Table:</h4>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="">

<h4>externale links Table:</h4>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="">

<h4>post attachement Table:</h4>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="">

<h4>Tags Table:</h4>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="">

<h4>Mention Table:</h4>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="">

<h3>Step 2: Insert Data into hbase Table From MapReduicer</h3>
<p>In this step, I'll execute my MapReduce jobs using Hadoop Streaming to store processed data in the HBase table</p>

<h4>user :</h4>

<pre><code>hadoop jar Documents/hadoop-streaming-2.7.3.jar -input /Mostodon/Raw/mastodon_data_2023-10-21.json -output /Mostodon/user -mapper /home/hadoop/MP/utilisateure_mapper.py -reducer /home/hadoop/MP/utilisateure_reducer.py</code></pre>

<b>resulte :</b>

<img width="687" alt="user table" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/bee7eba8-ee03-4af0-83b9-6053c276b1d2">

<h4>Content language Table:</h4>

<pre><code>hadoop jar Documents/hadoop-streaming-2.7.3.jar -input /Mostodon/Raw/mastodon_data_2023-10-21.json -output /Mostodon/language_counter -mapper /home/hadoop/MP/analyse_langue_mapper.py -reducer /home/hadoop/MP/analyse_langue_reducer.py</code>
</pre>

<b>resulte :</b>

<img width="620" alt="language" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/248b4a39-3dc1-41f5-af27-bdfe258b6c46">


<h4>externale links Table:</h4>

<pre><code>hadoop jar Documents/hadoop-streaming-2.7.3.jar -input /Mostodon/Raw/mastodon_data_2023-10-21.json -output /Mostodon/exiternal_sites -mapper /home/hadoop/MP/external_sites_mapper.py -reducer /home/hadoop/MP/external_sites_reducer.py</code>
</pre>

<b>resulte :</b>

<img width="619" alt="websites" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/c6bd1c5d-9489-4d41-b790-0ae499c6e344">


<h4>post attachement Table:</h4>

<pre><code>hadoop jar Documents/hadoop-streaming-2.7.3.jar -input /Mostodon/Raw/mastodon_data_2023-10-21.json -output /Mostodon/media_attachements -mapper /home/hadoop/MP/attachments_mapper.py -reducer /home/hadoop/MP/attachments_reducer.py</code></pre>

<b>resulte :</b>

<img width="616" alt="post attachment" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/70879acb-84af-4499-8f8b-adef2ea7dbe6">


<h4>Tags Mention Table:</h4>
<pre>
<code>hadoop jar Documents/hadoop-streaming-2.7.3.jar -input /Mostodon/Raw/mastodon_data_2023-10-21.json -output /Mostodon/tags_mention_user -mapper /home/hadoop/MP/tag_user_mapper.py -reducer /home/hadoop/MP/tag_user_reducer.py</code>
</pre>

<b>resulte :</b>

<img width="578" alt="tags" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/e980b725-1197-4b8d-a128-aa82490d4a3c">

<img width="559" alt="mentions" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/05ebe667-0c14-4869-8b58-fadc4f630fb9">

<h4>My HDFS files:</h4>

<img width="559" alt="mentions" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/b4ddbb1a-6df4-4908-af6e-8f4b3cdd1bf3">

<img width="559" alt="mentions" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/5519862c-fd76-4d9a-b490-46f8d91eed02">

<h2 class="code-line" data-line-start=123 data-line-end=124 ><a id="Data_Storage_with_HBa_123"></a>Mastodon Data analyse :</h2>
In this step, I will analyze my HBase data from my tables 
<h4>User analyse :</h4>
<h5>Top User Has Followers :</h5>
<img width="305" alt="analyse followers" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/c91a2e55-6475-4aef-a154-29518f712bfd">

<h5>Analyze user engagement rate:</h5>
<img width="305" alt="analyse followers" src="">

<h5>Analyze user growth:</h5>
<img width="305" alt="analyse followers" src="">

<h4>Content analysis:</h4>
<h5>Analyze external websites:</h5>
<img width="305" alt="analyse followers" src="">

<h5>Language Analysis:</h5>
<img width="305" alt="analyse followers" src="">

<h5>Media Engagement Analysis:</h5>
<img width="305" alt="analyse followers" src="">

<h5>Analysis of tags and mentions:</h5>
<img width="305" alt="analyse followers" src="">


<h2 class="code-line" data-line-start=123 data-line-end=124 ><a id="Data_Storage_with_HBa_123"></a>Airflow</h2>
<h3 class="code-line" data-line-start=0 data-line-end=1 ><a id="Workflow_Overview_0"></a>Workflow Overview</h3>
<p class="has-line-data" data-line-start="1" data-line-end="2">The data processing workflow consists of the following key steps:</p>
<ol>
<li class="has-line-data" data-line-start="3" data-line-end="5">
<p class="has-line-data" data-line-start="3" data-line-end="4"><strong>Data Extraction from Mastodon</strong>: In this initial step, Python scripts are used to extract data from Mastodon social media.</p>
</li>
<li class="has-line-data" data-line-start="5" data-line-end="7">
<p class="has-line-data" data-line-start="5" data-line-end="6"><strong>HBase Table Creation</strong>: After data extraction, a new HBase table is created to store the data.</p>
</li>
<li class="has-line-data" data-line-start="7" data-line-end="9">
<p class="has-line-data" data-line-start="7" data-line-end="8"><strong>Data Transformation</strong>: The extracted data is transformed to fit the HBase schema and format.</p>
</li>
<li class="has-line-data" data-line-start="9" data-line-end="11">
<p class="has-line-data" data-line-start="9" data-line-end="10"><strong>MapReduce Job for Data Insertion</strong>: A MapReduce job is used to efficiently insert data into the HBase table.</p>
</li>
<li class="has-line-data" data-line-start="11" data-line-end="12">
<p class="has-line-data" data-line-start="11" data-line-end="12"><strong>Data Analysis</strong>: Following data insertion, Python scripts are employed to analyze the data.</p>
</li>
</ol>
<p class="has-line-data" data-line-start="0" data-line-end="1">It seems like you want to document a part of your workflow that involves creating a DAG (Directed Acyclic Graph) file to execute your workflow daily at 23:00 and archive the latest data. Here’s how you can document it:</p> <h1 class="code-line" data-line-start=2 data-line-end=3 ><a id="DAG_Creation_for_Daily_Workflow_Execution_2"></a>DAG Creation for Daily Workflow Execution</h1> <h2 class="code-line" data-line-start=4 data-line-end=5 ><a id="Introduction_4"></a>Introduction</h2> <p class="has-line-data" data-line-start="5" data-line-end="6">This section outlines the process of creating a DAG (Directed Acyclic Graph) file to schedule the execution of your workflow. The workflow is scheduled to run once daily at 23:00, and it includes archiving the most recent data.</p> <h2 class="code-line" data-line-start=7 data-line-end=8 ><a id="Workflow_Overview_7"></a>Workflow Overview</h2> <p class="has-line-data" data-line-start="8" data-line-end="9">The key elements of this step include:</p> <ol> <li class="has-line-data" data-line-start="10" data-line-end="12"> <p class="has-line-data" data-line-start="10" data-line-end="11"><strong>DAG File Creation</strong>: A DAG file is created to define the workflow’s structure, schedule, and tasks.</p> </li> <li class="has-line-data" data-line-start="12" data-line-end="14"> <p class="has-line-data" data-line-start="12" data-line-end="13"><strong>Daily Execution</strong>: The DAG file is scheduled to run daily at 23:00, ensuring that the workflow is executed at the specified time.</p> </li> <li class="has-line-data" data-line-start="14" data-line-end="16"> <p class="has-line-data" data-line-start="14" data-line-end="15"><strong>Data Archiving</strong>: As part of the workflow, the most recent data is archived for future reference or analysis.</p> </li> </ol> <h2 class="code-line" data-line-start=16 data-line-end=17 ><a id="Step_1_DAG_File_Creation_16"></a>Step 1: DAG File Creation</h2> <p class="has-line-data" data-line-start="17" data-line-end="18">In this step, a DAG file is created using Apache Airflow. The DAG file defines the workflow’s structure and includes details about the tasks, dependencies, and scheduling.</p> <h2 class="code-line" data-line-start=19 data-line-end=20 ><a id="Step_2_Daily_Execution_19"></a>Step 2: Daily Execution</h2> <p class="has-line-data" data-line-start="20" data-line-end="21">The DAG is configured to execute the workflow once every day, precisely at 23:00. This ensures that your workflow runs at the specified time without manual intervention.</p> <h2 class="code-line" data-line-start=22 data-line-end=23 ><a id="Step_3_Data_Archiving_22"></a>Step 3: Data Archiving</h2> <p class="has-line-data" data-line-start="23" data-line-end="24">As part of the workflow, the most recent data is archived. This may involve saving data to a specific storage location or creating backups for future reference or analysis.</p> 


