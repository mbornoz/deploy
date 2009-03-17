import logging
logger = logging.getLogger('deploy.remote')

def remote_copy(src, host):
    logger.info("copying '%(src)s' to '%(host)s'"%{'src': src, 'host': host})
    cmd = "rsync -avz "
    # rsync -avz 
    return True

def remote_extract(dir, host):
    #logger.info("start extracting '%(project)s' at '%(host)s'"%{'project': project, 'host': host})
    cmd = "ssh %(host)s deploy -x %(dir)s" % {'host': host, 'dir': dir}
    logger.info("running '%(cmd)s'"%{'cmd': cmd})
    return True
