#!/bin/bash

# augment.sh -> Script to install all the packages for dataset augmentation

##### Constants

ROOT_DIR=$(pwd)
PROXY="http://192.168.16.67:3128"

##### Global variables
proxy_active=false

##### Functions

initialization()
{
   
   # Set proxy if mode -p is requested, else unset proxy
   if [ "$proxy_active" = true ] ; then
       export http_proxy="$PROXY"
       export https_proxy="$PROXY"
   else
       unset http_proxy
       unset https_proxy
   fi
   

  }


install_packages()
{
   pip3 install albumentations 
}

run()
{
  echo "Working...."
  python3 divide_dataset.py
  python3 augment.py
  python3 divide_original_augmented.py
  chmod -R 777 dataset
  echo "Done!!"
}


usage()
{
   echo "     -p             -> Set default proxy"    
   echo "     -p={IP:PUERTO} -> Set proxy (Default -> http://192.168.16.67:3128)"
}



##### Main
exec_proxy=false
exec_initialization=false
exec_install_packages=false
exec_run=false


if [ $# -gt 0 ]; then
   for i in "$@"
   do
      case $i in
         -p=* | --proxy=* )      PROXY="${i#*=}"
                                 exec_proxy=true
                                 exec_initialization=true
                                 exec_install_packages=true
                                 exec_run=true
                                 ;;
         -p | --proxy )          exec_proxy=true
                                 exec_initialization=true
                                 exec_install_packages=true
                                 exec_run=true
                                 ;;
      esac
      shift
   done
else
   exec_initialization=true
fi


if [ "$exec_proxy" = true ] ; then
    proxy_active=true
fi

if [ "$exec_initialization" = true ] ; then
    initialization
fi


if [ "$exec_install_packages" = true ] ; then
    install_packages 
fi


if [ "$exec_run" = true ] ; then
    run 
fi

