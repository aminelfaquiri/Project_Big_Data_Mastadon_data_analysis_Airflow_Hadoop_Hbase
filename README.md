<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Project_Big_Data_Mastodon_Data_Analysis_with_Airflow_Hadoop_and_HBase_0"></a>Project Big Data Mastodon Data Analysis with Airflow, Hadoop, and HBase</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Introduction_2"></a>Introduction</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">This project is dedicated to the analysis of data from the Mastodon platform and aims to address various critical needs for the extraction, processing, and analysis of massive data. As a data developer, the mission is to establish an automated pipeline to tackle these complex challenges. This project responds to the necessity of extracting meaningful insights from raw Mastodon data, focusing on user analysis, content analysis, language analysis, media engagement, tags, mentions, and more. To achieve this, several key steps need to be followed, from raw data collection to in-depth analysis of the results. These needs define the framework of this Big Data project and will be detailed in the following sections.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Planning_6"></a>Planning</h2>
<h3 class="code-line" data-line-start=8 data-line-end=9 ><a id="Requirements_Expression__8"></a>Requirements Expression :</h3>
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
<h3 class="code-line" data-line-start=21 data-line-end=22 ><a id="Environment___21"></a>Environment  :</h3>
<h4 class="code-line" data-line-start=23 data-line-end=24 ><a id="Hadoop_Installation__23"></a>Hadoop Installation :</h4>
<h4 class="code-line" data-line-start=25 data-line-end=26 ><a id="HBase_Installation_25"></a>HBase Installation</h4>
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
<h4 class="code-line" data-line-start=117 data-line-end=118 ><a id="Airflow_Installation__117"></a>Airflow Installation :</h4>
<h2 class="code-line" data-line-start=119 data-line-end=120 ><a id="Data_Collection_119"></a>Data Collection</h2>
<h2 class="code-line" data-line-start=121 data-line-end=122 ><a id="MapReduce_Processing_121"></a>MapReduce Processing</h2>
<h2 class="code-line" data-line-start=123 data-line-end=124 ><a id="Data_Storage_with_HBa_123"></a>Data Storage with HBa</h2>
