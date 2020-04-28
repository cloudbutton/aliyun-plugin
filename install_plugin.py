import pywren_ibm_cloud
import os
import shutil

module_location = os.path.dirname(os.path.abspath(pywren_ibm_cloud.__file__))
dst_storage_backend_path = os.path.join(module_location, 'storage', 'backends', 'aliyun_oss')
dst_compute_backend_path = os.path.join(module_location, 'compute', 'backends', 'aliyun_fc')

if os.path.isdir(dst_storage_backend_path):
    shutil.rmtree(dst_storage_backend_path)
elif os.path.isfile(dst_storage_backend_path):
    os.remove(dst_storage_backend_path)

if os.path.isdir(dst_compute_backend_path):
    shutil.rmtree(dst_compute_backend_path)
elif os.path.isfile(dst_compute_backend_path):
    os.remove(dst_compute_backend_path)

current_location = os.path.dirname(os.path.abspath(__file__))
src_storage_backend_path = os.path.join(current_location, 'storage', 'backends', 'aliyun_oss')
src_compute_backend_path = os.path.join(current_location, 'compute', 'backends', 'aliyun_fc')

shutil.copytree(src_storage_backend_path, dst_storage_backend_path)
shutil.copytree(src_compute_backend_path, dst_compute_backend_path)
