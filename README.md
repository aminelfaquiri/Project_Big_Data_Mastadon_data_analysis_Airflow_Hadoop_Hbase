<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Project_Big_Data_Mastodon_Data_Analysis_with_Airflow_Hadoop_and_HBase_0"></a>Projet Analyse de données Mastodon Big Data avec Airflow, Hadoop et HBase</h1>
<h2 class="code-line" data-line-start=2 data-line-end=3 ><a id="Introduction_2"></a>Introduction</h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">Ce projet est dédié à l'analyse des données de la plateforme Mastodon et vise à répondre à divers besoins critiques pour l'extraction, le traitement et l'analyse de données massives. En tant que développeur de données, la mission est d'établir un pipeline automatisé pour relever ces défis complexes. Ce projet répond à la nécessité d'extraire des informations significatives à partir des données brutes de Mastodon, en mettant l'accent sur l'analyse des utilisateurs, l'analyse du contenu, l'analyse du langage, l'engagement des médias, les balises, les mentions, etc. Pour ce faire, plusieurs étapes clés doivent être suivies, de la collecte des données brutes à l'analyse approfondie des résultats. Ces besoins définissent le cadre de ce projet Big Data et seront détaillés dans les sections suivantes.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Planning_6"></a>Planification</h2>
<h3 class="code-line" data-line-start=8 data-line-end=9 ><a id="Requirements_Expression__8"></a>Expression des besoins :</h3>
<ul>
<li class="has-line-data" data-line-start="10" data-line-end="11"><strong>Collecte de données :</strong> Utilisation de l'API Mastodon, stockage des données dans HDFS et modélisation du Data Lake HDFS.</li>
<li class="has-line-data" data-line-start="11" data-line-end="12"><strong>Traitement MapReduce :</strong> Mappage et réduction pour transformer et agréger les données.</li>
<li class="has-line-data" data-line-start="12" data-line-end="13"><strong>Exécution des travaux MapReduce :</strong> Utilisation de l'API de streaming Hadoop et suivi via l'interface Web Hadoop.</li>
<li class="has-line-data" data-line-start="13" data-line-end="14"><strong>Stockage des résultats dans HBase :</strong> Conception du schéma HBase, création de tables et insertion de données.</li>
<li class="has-line-data" data-line-start="14" data-line-end="15"><strong>Orchestration avec Apache Airflow :</strong> Définition d'un DAG, création de tâches et suivi via Airflow.</li>
<li class="has-line-data" data-line-start="15" data-line-end="16"><strong>Analyse des résultats :</strong> Interrogation des données dans HBase pour extraire des informations sur les utilisateurs, le contenu, le langage, l'engagement des médias, les balises et les mentions.</li>
<li class="has-line-data" data-line-start="16" data-line-end="17"><strong>Optimisation et surveillance :</strong> Optimisation des scripts MapReduce, surveillance de HBase, configuration d'alertes Airflow et surveillance de Hadoop.</li>
<li class="has-line-data" data-line-start="17" data-line-end="18"><strong>Mise à jour des autorisations et de la documentation :</strong> Mise à jour des jetons d'API, documentation des rôles, des autorisations et des règles d'accès.</li>
<li class="has-line-data" data-line-start="18" data-line-end="19"><strong>Développements planifiés :</strong> Planification régulière des DAG pour maintenir les données à jour.</li>
<li class="has-line-data" data-line-start="19" data-line-end="21"><strong>Conformité au RGPD :</strong> Documentation des données personnelles, conformité aux réglementations RGPD.</li>
</ul>
<h3 class="code-line" data-line-start=21 data-line-end=22 ><a id="Environment___21"></a>Environnement  :</h3>
<h1 class="code-line" data-line-start=2 data-line-end=3 ><a id="Hadoop_Installation_Script_2"></a>Script d'installation de Hadoop</h1>
<p class="has-line-data" data-line-start="4" data-line-end="5">Ce script vous guide à travers l'installation de Hadoop sur Ubuntu. Il couvre l'installation de Java, de Hadoop, la configuration SSH et la mise en place de l'environnement nécessaire.</p>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Installation_de_Java_sur_Ubuntu_6"></a>Installation de Java sur Ubuntu</h2>
<pre><code class="has-line-data" data-line-start="9" data-line-end="13" class="language-bash">sudo apt install default-jre default-jdk -y
java -version
readlink $(<span class="hljs-built_in">which</span> javac)
</code></pre>
<h2 class="code-line" data-line-start=14 data-line-end=15 ><a id="Créer_un_utilisateur_pour_Hadoop_et_configurer_SSH_14"></a>Créer un utilisateur pour Hadoop et configurer SSH</h2>
<pre><code class="has-line-data" data-line-start="17" data-line-end="26" class="language-bash">sudo adduser hadoop
sudo usermod <span class="hljs-operator">-a</span>G sudo hadoop
sudo su - hadoop
sudo apt install openssh-server openssh-client -y
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub &gt;&gt; ~/.ssh/authorized_keys 
sudo chmod <span class="hljs-number">640</span> ~/.ssh/authorized_keys
ssh localhost
</code></pre>
<h2 class="code-line" data-line-start=27 data-line-end=28 ><a id="Télécharger_et_installer_Apache_Hadoop_sur_Ubuntu_27"></a>Télécharger et installer Apache Hadoop sur Ubuntu</h2>
<pre><code class="has-line-data" data-line-start="30" data-line-end="36" class="language-bash">wget https://dlcdn.apache.org/hadoop/common/hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>/hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>.tar.gz
tar -xvzf hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>.tar.gz
sudo mv hadoop-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span> /usr/local/hadoop
</code></pre>
<h2 class="code-line" data-line-start=37 data-line-end=38 ><a id="Configurer_Apache_Hadoop_37"></a>Configurer Apache Hadoop</h2>
<pre><code class="has-line-data" data-line-start="40" data-line-end="52" class="language-bash">echo 'export HADOOP_HOME=/usr/local/hadoop' &gt;&gt; ~/.bashrc
echo 'export PATH=$PATH:$HADOOP_HOME/bin' &gt;&gt; ~/.bashrc
echo 'export PATH=$PATH:$HADOOP_HOME/sbin' &gt;&gt; ~/.bashrc
source ~/.bashrc
</code></pre>
<h2 class="code-line" data-line-start=53 data-line-end=54 ><a id="Configuration_de_Hadoop_53"></a>Configuration de Hadoop</h2>
<pre><code class="has-line-data" data-line-start="56" data-line-end="77" class="language-bash">cd /usr/local/hadoop/etc/hadoop
sudo nano hadoop-env.sh
</code></pre>
<p class="has-line-data" data-line-start="78" data-line-end="79">Assurez-vous que la ligne suivante est dans le fichier hadoop-env.sh :</p>
<pre><code class="has-line-data" data-line-start="80" data-line-end="83" class="language-bash">export <span class="hljs-variable">JAVA_HOME</span>=/usr/lib/jvm/default-java
</code></pre>
<p class="has-line-data" data-line-start="84" data-line-end="85">Appuyez sur Ctrl+X, puis sur Y et appuyez sur Entrée pour sauvegarder le fichier.</p>
<p class="has-line-data" data-line-start="86" data-line-end="87">Ensuite, configurez les fichiers core-site.xml :</p>
<pre><code class="has-line-data" data-line-start="88" data-line-end="108" class="language-bash">sudo nano core-site.xml
</code></pre>
<p class="has-line-data" data-line-start="109" data-line-end="112">Ajoutez ce qui suit dans le fichier core-site.xml :</p>
<pre><code class="has-line-data" data-line-start="113" data-line-end="118" class="language-xml">&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;fs.defaultFS&lt;/name&gt;
    &lt;value&gt;hdfs://localhost:9000&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
</code></pre>
<p class="has-line-data" data-line-start="119" data-line-end="120">Enregistrez le fichier.</p>
<p class="has-line-data" data-line-start="121" data-line-end="122">Ensuite, configurez le fichier hdfs-site.xml :</p>
<pre><code class="has-line-data" data-line-start="123" data-line-end="144" class="language-bash">sudo nano hdfs-site.xml
</code></pre>
<p class="has-line-data" data-line-start="145" data-line-end="149">Ajoutez ce qui suit dans le fichier hdfs-site.xml :</p>
<pre><code class="has-line-data" data-line-start="150" data-line-end="157" class="language-xml">&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;dfs.replication&lt;/name&gt;
    &lt;value&gt;1&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
</code></pre>
<p class="has-line-data" data-line-start="158" data-line-end="159">Enregistrez le fichier.</p>
<p class="has-line-data" data-line-start="160" data-line-end="161">Ensuite, configurez le fichier mapred-site.xml :</p>
<pre><code class="has-line-data" data-line-start="162" data-line-end="183" class="language-bash">sudo nano mapred-site.xml
</code></pre>
<p class="has-line-data" data-line-start="184" data-line-end="191">Ajoutez ce qui suit dans le fichier mapred-site.xml :</p>
<pre><code class="has-line-data" data-line-start="192" data-line-end="201" class="language-xml">&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;mapreduce.framework.name&lt;/name&gt;
    &lt;value&gt;yarn&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
</code></pre>
<p class="has-line-data" data-line-start="202" data-line-end="203">Enregistrez le fichier.</p>
<p class="has-line-data" data-line-start="204" data-line-end="205">Enfin, configurez le fichier yarn-site.xml :</p>
<pre><code class="has-line-data" data-line-start="206" data-line-end="229" class="language-bash">sudo nano yarn-site.xml
</code></pre>
<p class="has-line-data" data-line-start="230" data-line-end="235">Ajoutez ce qui suit dans le fichier yarn-site.xml :</p>
<pre><code class="has-line-data" data-line-start="236" data-line-end="249" class="language-xml">&lt;configuration&gt;
  &lt;property&gt;
    &lt;name&gt;mapreduce.application.classpath&lt;/name&gt;
    &lt;value&gt;/usr/local/hadoop/etc/hadoop:/usr/local/hadoop/share/hadoop/common/*:/usr/local/hadoop/share/hadoop/common/lib/*:/usr/local/hadoop/share/hadoop/hdfs/*:/usr/local/hadoop/share/hadoop/hdfs/lib/*:/usr/local/hadoop/share/hadoop/mapreduce/*:/usr/local/hadoop/share/hadoop/mapreduce/lib/*:/usr/local/hadoop/share/hadoop/yarn/*:/usr/local/hadoop/share/hadoop/yarn/lib/*&lt;/value&gt;
  &lt;/property&gt;
&lt;/configuration&gt;
</code></pre>
<p class="has-line-data" data-line-start="250" data-line-end="251">Enregistrez le fichier.</p>
<p class="has-line-data" data-line-start="252" data-line-end="253">Vous avez maintenant configuré Hadoop avec succès.</p>
<h2 class="code-line" data-line-start=254 data-line-end=255 ><a id="Créer_un_utilisateur_HDFS_et_les_répertoires_de_base_254"></a>Créer un utilisateur HDFS et les répertoires de base</h2>
<pre><code class="has-line-data" data-line-start="257" data-line-end="276" class="language-bash">sudo hdfs namenode -format
sudo hdfs datanode -format
sudo chown -R <span class="hljs-variable">hadoop</span>:<span class="hljs-variable">hadoop</span> /usr/local/hadoop
sudo chown -R <span class="hljs-variable">hadoop</span>:<span class="hljs-variable">hadoop</span> /app/hadoop/tmp
</code></pre>
<p class="has-line-data" data-line-start="277" data-line-end="279">Vous devez créer un utilisateur hdfs en utilisant la commande suivante :</p>
<pre><code class="has-line-data" data-line-start="280" data-line-end="281" class="language-bash">sudo <span class="hljs-variable">hdfs</span> namenode -format
</code></pre>
<p class="has-line-data" data-line-start="282" data-line-end="284">Vous pouvez maintenant démarrer les services Hadoop :</p>
<pre><code class="has-line-data" data-line-start="285" data-line-end="292" class="language-bash">sudo <span class="hljs-variable">start-dfs</span>.sh
sudo <span class="hljs-variable">start-yarn</span>.sh
</code></pre>
<p class="has-line-data" data-line-start="293" data-line-end="294">Pour vérifier que tout fonctionne correctement, accédez à l'interface Web de Hadoop en ouvrant votre navigateur et en accédant à :</p>
<pre><code class="has-line-data" data-line-start="295" data-line-end="296" class="language-text">http://localhost:9870/
</code></pre>
<p class="has-line-data" data-line-start="297" data-line-end="298">Vous devriez voir l'interface de gestion de Hadoop.</p>
<h2 class="code-line" data-line-start=299 data-line-end=300 ><a id="Exécuter_un_exemple_Hadoop_299"></a>Exécuter un exemple Hadoop</h2>
<pre><code class="has-line-data" data-line-start="302" data-line-end="319" class="language-bash">sudo su - <span class="hljs-variable">hadoop</span>
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-<span class="hljs-number">3.3</span>.<span class="hljs-number">6</span>.jar wordcount <span class="hljs-variable">/user/hadoop/input</span> <span class="hljs-variable">/user/hadoop/output</span>
cat <span class="hljs-variable">/user/hadoop/output/part-r-00000</span>
exit
</code></pre>
<p class="has-line-data" data-line-start="320" data-line-end="322">Cela exécutera un exemple de comptage de mots à l'aide de Hadoop. Vous pouvez vérifier les résultats en utilisant la commande "cat".</p>
<p class="has-line-data" data-line-start="323" data-line-end="324">C'est tout ! Vous avez maintenant installé et configuré Apache Hadoop sur votre système.</p>
<h2 class="code-line" data-line-start=325 data-line-end=326 ><a id="Conclusion_325"></a>Conclusion</h2>
<p class="has-line-data" data-line-start="328" data-line-end="332">Hadoop est un framework puissant pour le traitement des données distribuées. Avec ces instructions, vous avez installé avec succès Hadoop sur votre système Ubuntu. Vous êtes maintenant prêt à commencer à utiliser Hadoop pour le traitement et l'analyse de données massives.</p>
<p class="has-line-data" data-line-start="333" data-line-end="336">N'oubliez pas que la configuration et l'utilisation de Hadoop peuvent devenir complexes, en particulier dans des environnements de production. Assurez-vous de consulter la documentation officielle de Hadoop pour en savoir plus sur ses fonctionnalités et ses possibilités.</p>

You can follow the steps outlined in the guide to install and configure Apache Hadoop on your Ubuntu 20.04 system. Here's a summary of the key steps:

1. **Prerequisites:**
   - Ensure that you have Java installed on your system.

2. **Download and Extract Hadoop:**
   - Download the Hadoop distribution (e.g., Hadoop 3.3.6) from the Apache Hadoop website.
   - Extract the downloaded archive and move it to the `/usr/local/hadoop` directory.

3. **Configure Hadoop:**
   - Set environment variables by adding the following lines to your `~/.bashrc` file:
     ```
     export HADOOP_HOME=/usr/local/hadoop
     export PATH=$PATH:$HADOOP_HOME/bin
     export PATH=$PATH:$HADOOP_HOME/sbin
     ```
   - Source the `~/.bashrc` file to apply the changes.

4. **Configuration Files:**
   - Configure `hadoop-env.sh` to set the `JAVA_HOME` environment variable.
   - Configure `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, and `yarn-site.xml` with the necessary properties.

5. **Create an HDFS User and Basic Directories:**
   - Create an HDFS user: `sudo hdfs namenode -format`
   - Change ownership of directories:
     ```
     sudo chown -R hadoop:hadoop /usr/local/hadoop
     sudo chown -R hadoop:hadoop /app/hadoop/tmp
     ```

6. **Start Hadoop Services:**
   - Start Hadoop services:
     ```
     sudo start-dfs.sh
     sudo start-yarn.sh
     ```

7. **Test with a Hadoop Example:**
   - Run a Hadoop example using the WordCount program.

8. **Conclusion:**
   - You've successfully installed and configured Apache Hadoop on your Ubuntu system. Be sure to consult the official Hadoop documentation for more advanced usage and configurations.

Remember that Hadoop configurations can become complex, especially in production environments. You may need further customization and tuning for your specific use case.
