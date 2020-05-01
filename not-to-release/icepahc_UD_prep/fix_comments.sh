
pattern1="# IcePaHC_ID"
pattern2="# sent_id"

sed -e :a \
    -e "\$!N; s/^\(.*${pattern1}.*\)\n\(.*${pattern2}.*\)/\2\n\1/;ta" \
    -e 'P;D' < ../../out/is_icepahc-ud-dev.conllu
