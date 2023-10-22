<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Project_Big_Data_Mastodon_Data_Analysis_with_Airflow_Hadoop_and_HBase_0"></a>Projet d'analyse de données Mastodon Big Data avec Airflow, Hadoop et HBase</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Introduction_2"></a>Introduction</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">Ce projet est dédié à l'analyse des données de la plateforme Mastodon et vise à répondre à divers besoins essentiels pour l'extraction, le traitement et l'analyse de données massives. En tant que développeur de données, la mission consiste à mettre en place un pipeline automatisé pour relever ces défis complexes. Ce projet répond à la nécessité d'extraire des informations significatives à partir des données brutes de Mastodon, en mettant l'accent sur l'analyse des utilisateurs, l'analyse du contenu, l'analyse linguistique, l'engagement multimédia, les balises, les mentions, etc. Pour y parvenir, plusieurs étapes clés doivent être suivies, de la collecte de données brutes à l'analyse approfondie des résultats. Ces besoins définissent le cadre de ce projet Big Data et seront détaillés dans les sections suivantes.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Planning_6"></a>Planification</h2>
<img width="540" alt="Capture d'écran 2023-10-20 222858" src="https://github.com/aminelfaquiri/Project_Big_Data_Mastadon_data_analysis_Airflow_Hadoop_Hbase/assets/81482544/f38055c4-189b-4e8a-9cb5-be758231c2f4">

<h2 class="code-line" data-line-start=8 data-line-end=9 ><a id="Requirements_Expression__8"></a>Expression des besoins :</h3>
<ul>
<li class="has-line-data" data-line-start="10" data-line-end="11"><strong>Collecte de données :</strong> Utilisation de l'API Mastodon, stockage des données dans HDFS et modélisation du Data Lake HDFS.</li>
<li class="has-line-data" data-line-start="11" data-line-end="12"><strong>Traitement MapReduce :</strong> Mapper et réducteur pour transformer et agréger les données.</li>
<li class="has-line-data" data-line-start="12" data-line-end="13"><strong>Exécution des tâches MapReduce :</strong> Utilisation de l'API de streaming Hadoop et suivi via l'interface Web Hadoop.</li>
<li class="has-line-data" data-line-start="13" data-line-end="14"><strong>Stockage des résultats dans HBase :</strong> Conception du schéma HBase, création de tables et insertion des données.</li>
<li class="has-line-data" data-line-start="14" data-line-end="15"><strong>Orchestration avec Apache Airflow :</strong> Définition d'un DAG, création de tâches et suivi via Airflow.</li>
<li class="has-line-data" data-line-start="15" data-line-end="16"><strong>Analyse des résultats :</strong> Interrogation des données dans HBase pour extraire des informations sur les utilisateurs, le contenu, la langue, l'engagement multimédia, les balises et les mentions.</li>
<li class="has-line-data" data-line-start="16" data-line-end="17"><strong>Optimisation et surveillance :</strong> Optimisation des scripts MapReduce, surveillance de HBase, configuration d'alertes Airflow et surveillance de Hadoop.</li>
<li class="has-line-data" data-line-start="17" data-line-end="18"><strong>Mise à jour des autorisations et de la documentation :</strong> Mise à jour des jetons d'API, documentation des rôles, des autorisations et des règles d'accès.</li>
<li class="has-line-data" data-line-start="18" data-line-end="19"><strong>Développements planifiés :</strong> Programmation régulière des DAG pour maintenir les données à jour.</li>
<li class="has-line-data" data-line-start="19" data-line-end="21"><strong>Conformité au RGPD :</strong> Documentation des données personnelles, conformité aux réglementations RGPD.</li>
</ul>
<h2 class="code-line" data-line-start=21 data-line-end=22 ><a id="Environnement___21"></a>Environnement  :</h2>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="Script_d'installation_de_Hadoop_2"></a>Script d'installation de Hadoop</h3>
<p class="has-line-data" data-line-start="4" data-line-end="5">Ce script vous guide dans l'installation de Hadoop sur Ubuntu. Il couvre l'installation de Java, de Hadoop, la configuration SSH et la mise en place de l'environnement nécessaire.</p>
<h4 class="code-line" data-line-start=6 data-line-end=7 ><a id="Installation_de_Java_sur_Ubuntu_6"></a>Installation de Java sur Ubuntu</h4>
<pre><code class="has-line-data" data-line-start="9" data-line-end="13" class="language-bash">sudo apt install default-jre default-jdk -y
java -version
readlink $(<span class="hljs-built_in">which</span> javac)
</code></pre>
<h4 class="code-line" data-line-start=14 data-line-end=15 ><a id="Créer_un_utilisateur_pour_Hadoop_et_configurer_SSH_14"></a>Créer un utilisateur pour Hadoop et configurer SSH</h4>
<pre><code class="has-line-data" data-line-start="17" data-line-end="26" class="language-bash">sudo adduser hadoop
sudo usermod <span class="hljs-operator">-a</span>G sudo hadoop
sudo su - hadoop
sudo apt install openssh-server openssh-client -y
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub &gt;&gt; ~/.ssh/authorized_keys 
sudo chmod <span class="hljs-number">640</span> ~/.ssh/authorized_keys
ssh localhost
</code></pre>
<h4 class="code-line" data-line-start=27 data-line-end=28 ><a id="Télécharger_et_extraire_Hadoop_27"></a>Télécharger et extraire Hadoop</h4>
<pre><code class="has-line-data" data-line-start="30" data-line-end="37" class="language-bash">wget <span class="hljs-string">https://apache.claz.org/hadoop/common/hadoop-3.3.0/hadoop-3.3.0.tar.gz</span>
tar -xvf hadoop-3.3.0.tar.gz
sudo mv hadoop-3.3.0 /usr/local/hadoop
rm hadoop-3.3.0.tar.gz
</code></pre>
<p class="has-line-data" data-line-start="38" data-line-end="39">Assurez-vous de télécharger la dernière version d'Hadoop à partir du site Web Apache.</p>
<p class="has-line-data" data-line-start="40" data-line-end="41">Référence : https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html</p>

<h3 class="code-line" data-line-start=3 data-line-end=4 ><a id="Script_d'installation_de_HBase_3"></a>Script d'installation de HBase</h3>
<p class="has-line-data" data-line-start="5" data-line-end="6">Ce script vous guide dans l'installation de HBase sur Ubuntu. Il couvre l'installation de HBase, de Java, la configuration de HBase et la création d'une table.</p>
<h4 class="code-line" data-line-start=7 data-line-end=8 ><a id="Installation_de_Java_sur_Ubuntu_7"></a>Installation de Java sur Ubuntu</h4>
<pre><code class="has-line-data" data-line-start="10" data-line-end="13" class="language-bash">sudo apt install default-jre default-jdk -y
java -version
readlink $(<span class="hljs-built_in">which</span> javac)
</code></pre>
<h4 class="code-line" data-line-start=14 data-line-end=15 ><a id="Télécharger_et_extraire_HBase_14"></a>Télécharger et extraire HBase</h4>
<pre><code class="has-line-data" data-line-start="17" data-line-end="26" class="language-bash">wget <span class="hljs-string">https://apache.claz.org/hbase/2.4.8/hbase-2.4.8-bin.tar.gz</span>
tar -xvf hbase-2.4.8-bin.tar.gz
sudo mv hbase-2.4.8 /usr/local/hbase
rm hbase-2.4.8-bin.tar.gz
</code></pre>
<p class="has-line-data" data-line-start="27" data-line-end="28">Assurez-vous de télécharger la dernière version de HBase depuis le site Web Apache.</p>
<p class="has-line-data" data-line-start="29" data-line-end="30">Référence : https://hbase.apache.org/book.html#quickstart</p>
<h4 class="code-line" data-line-start=31 data-line-end=32 ><a id="Configurer_HBase_31"></a>Configurer HBase</h4>
<p class="has-line-data" data-line-start="33" data-line-end="34">Modifiez le fichier de configuration hbase-site.xml pour configurer HBase. Exemple :</p>
<pre><code class="has-line-data" data-line-start="35" data-line-end="52" class="language-xml"> &lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.rootdir&lt;/name&gt;
    &lt;value&gt>hdfs://localhost:9000/hbase</value>
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.zookeeper.property.dataDir&lt;/name&gt;
    &lt;value&gt;/usr/local/hbase/zookeeper</value>
  &lt;/property&gt;
  &lt;property&gt;
    &lt;name&gt;hbase.cluster.distributed&lt;/name&gt;
    &lt;value&gt>true</value>
  &lt;/property&gt;
&lt;/configuration&gt;
</code></pre>
<h4 class="code-line" data-line-start=53 data-line-end=54 ><a id="Créer_une_table_HBase_53"></a>Créer une table HBase</h4>
<pre><code class="has-line-data" data-line-start="56" data-line-end="63" class="language-bash">sudo /usr/local/hbase/bin/start-hbase.sh
sudo /usr/local/hbase/bin/hbase shell
create '<span class="hljs-string">mastodon</span>', '<span class="hljs-string">content</span>', '<span class="hljs-string">metrics</span>'
</code></pre>
<p class="has-line-data" data-line-start="64" data-line-end="65">Cela crée une table HBase nommée "mastodon" avec des colonnes de famille "content" et "metrics".</p>
<p class="has-line-data" data-line-start="66" data-line-end="67">Référence : https://hbase.apache.org/book.html#quickstart</p>
<h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="Script_de_provisionnement_5"></a>Script de provisionnement</h2>
<p class="has-line-data" data-line-start="7" data-line-end="8">Ce script détaille le processus de provisionnement du projet, y compris la création du DAG Apache Airflow, la configuration des tâches MapReduce, la surveillance des composants, la planification des tâches et l'ajout de scripts aux tâches.</p>
<p class="has-line-data" data-line-start="9" data-line-end="10">Pour obtenir des instructions détaillées sur la configuration et le provisionnement, veuillez consulter le script complet dans le référentiel GitHub du projet.</p>
<p class="has-line-data" data-line-start="11" data-line-end="12">Référence : https://github.com/aminelfaquiri/Project_Big_Data_Mastodon_data_analysis_Airflow_Hadoop_Hbase</p>
<h2 class="code-line" data-line-start=12 data-line-end=13 ><a id="Guide_d'utilisation_12"></a>Guide d'utilisation</h2>
<p class="has-line-data" data-line-start="14" data-line-end="15">Pour utiliser ce projet, suivez les étapes ci-dessous :</p>
<h4 class="code-line" data-line-start=16 data-line-end=17 ><a id="Prérequis_16"></a>Prérequis</h4>
<ul>
<li class="has-line-data" data-line-start="17" data-line-end="18">Un cluster Hadoop fonctionnel.</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">Un cluster HBase fonctionnel.</li>
<li class="has-line-data" data-line-start="19" data-line-end="20">Un cluster Apache Airflow fonctionnel.</li>
</ul>
<h4 class="code-line" data-line-start=20 data-line-end=21 ><a id="Instructions_20"></a>Instructions</h4>
<ol>
<li class="has-line-data" data-line-start="21" data-line-end="22">Clonez le référentiel GitHub du projet : <code>git clone https://github.com/aminelfaquiri/Project_Big_Data_Mastodon_data_analysis_Airflow_Hadoop_Hbase.git</code></li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Suivez les étapes du "Script de provisionnement" pour configurer votre environnement de projet.</li>
<li class="has-line-data" data-line-start="23" data-line-end="24">Exécutez des tâches Airflow pour analyser les données Mastodon.</li>
</ol>
<p class="has-line-data" data-line-start="25" data-line-end="26">Référence : https://github.com/aminelfaquiri/Project_Big_Data_Mastodon_data_analysis_Airflow_Hadoop_Hbase</p>

<h2 class="code-line" data-line-start=27 data-line-end=28 ><a id="Contributeurs_27"></a>Contributeurs</h-line-data"> data-line-start="29" data-line-end="30">Voici les contributeurs principaux de ce projet :</p>
<ul>
<li class="has-line-data" data-line-start="31" data-line-end="32">Amine Lfaquiri - Auteur principal</li>
</ul>
<p class="has-line-data" data-line-start="33" data-line-end="34">Merci à toutes les personnes qui ont contribué à ce projet !</p>
<p class="has-line-data" data-line-start="35" data-line-end="36">Référence : https://github.com/aminelfaquiri/Project_Big_Data_Mastodon_data_analysis_Airflow_Hadoop_Hbase/graphs/contributors</p>
