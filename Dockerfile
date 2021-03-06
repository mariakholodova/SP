FROM ubuntu
COPY sp2.sh .
RUN chmod ugo+x sp2.sh
CMD ./sp2.sh
