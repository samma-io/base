from ubuntu


#Install nmap

RUN apt-get update && apt-get install git nmap python3-pip python3-geoip wget unzip -y
WORKDIR /opt
#dns spider
RUN wget https://github.com/nullsecuritynet/tools/raw/master/scanner/dnsspider/release/dnsspider-1.3.tar.gz
RUN tar zxvf dnsspider-1.3.tar.gz
RUN pip3 install dnspython

# /opt/dnsspider-1.3/dnsspider.py -t 0 -a $TARGET

# webanalyser
RUN apt-get install python3 python3-dnspython -y
#RUN pip install geoip
RUN wget https://github.com/eldraco/domain_analyzer/archive/refs/heads/master.zip
RUN unzip master.zip

#./opt/domain_analyzer/crawler.py -u $TARGET
#


#recon-ng
RUN git clone https://github.com/lanmaster53/recon-ng.git
WORKDIR /opt/recon-ng
RUN pip install -r REQUIREMENTS



# Setup Run
RUN mkdir /code
RUN mkdir /output
RUN mkdir /out


WORKDIR /code
COPY code/ .

RUN chmod 555 -R /code
RUN useradd -ms /bin/bash samma

RUN chown samma:samma /out
RUN chown samma:samma /output
RUN chown samma:samma -R /opt/domain_analyzer-master
RUN chmod 775 -R /opt/domain_analyzer-master
RUN chmod +x /code/run.sh


USER samma
WORKDIR /output 

CMD /code/run.sh


