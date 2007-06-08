def MoveFile(orig, new, mode):
    import os
    import shutil
 
    try:
        shutil.copyfile(orig,new)
    except IOError, e:
        Error = e.strerror
        return False
 
    try:
        os.chmod(new,mode)
    except OSError, e:
        Error = e.strerror
        return False
 
    try:
        os.unlink(orig)
    except OSError, e:
        Error = e.strerror
        return False
 
    return True;
