FROM library/ubuntu:latest
MAINTAINER Euxhen Hasanaj ehasanaj@cs.cmu.edu

### Install apps
RUN apt-get update

# Install tzdata
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get install -y\
    python3\
    python3-pip\
    git\
    libcurl4-openssl-dev\
    libssl-dev\
    wget\
    libxml2-dev\
    xvfb\
    libgtk2.0\
    libgconf-2-4\
    libnss3

RUN apt-get install -y software-properties-common

### Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com\
                --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
RUN apt install -y r-base r-base-core r-recommended r-base-dev

### Install R libraries
RUN Rscript -e 'install.packages("shiny")'
RUN Rscript -e 'install.packages("shinydashboard")'
RUN Rscript -e 'install.packages("shinyjs")'
RUN Rscript -e 'install.packages("shinyBS")'
RUN Rscript -e 'install.packages("reticulate")'
RUN Rscript -e 'install.packages("ggplot2")'
RUN Rscript -e 'install.packages("plotly")'
RUN Rscript -e 'install.packages("rjson")'
RUN Rscript -e 'install.packages("DT")'
RUN Rscript -e 'install.packages("gplots")'
RUN Rscript -e 'install.packages("bsplus")'
RUN Rscript -e 'install.packages("BiocManager")'
RUN Rscript -e 'BiocManager::install("SingleR")'
RUN Rscript -e 'install.packages("htmlTable")'

# Install orca dependency for plotly
RUN wget https://github.com/plotly/orca/releases/download/v1.1.1/orca-1.1.1-x86_64.AppImage -P /opt
RUN chmod 777 /opt/orca-1.1.1-x86_64.AppImage
RUN cd /opt && /opt/orca-1.1.1-x86_64.AppImage --appimage-extract
RUN printf '#!/bin/bash \nxvfb-run --auto-servernum --server-args "-screen 0 640x480x24" /opt/squashfs-root/app/orca "$@"' > /usr/bin/orca
RUN chmod 777 /usr/bin/orca

### Install Cluster Ensembles
RUN dpkg --add-architecture i386
RUN apt-get install -y metis libc6-i386
RUN pip3 install git+https://github.com/ferrocactus/Cluster_Ensembles
RUN echo "export PATH=$PATH:/usr/local/lib/python3.8/dist-packages/Cluster_Ensembles/Hypergraph_Partitioning/hmetis-1.5-linux/" >> /root/.bashrc

RUN apt-get clean

EXPOSE 23123

RUN git clone https://github.com/ferrocactus/cellar /home/cellar
### Install python3 dependencies
RUN pip3 install -r /home/cellar/py_requirements.txt

WORKDIR /home/cellar
# Compile Cython modules
RUN python3 src/methods/setup.py build_ext --inplace
RUN python3 src/methods/setup.py clean

RUN mkdir -p datasets/user_uploaded
RUN mkdir -p datasets/server

ADD https://api.github.com/repos/ferrocactus/cellar/git/refs/heads/master version.json
RUN git pull

ENTRYPOINT ["Rscript", "app.R"]
