# CloudButton Alibaba Cloud (Aliyun) Plugin
Cloudbutton toolkit plugin for Aliyun Function Compute and Aliyun Object Storage Service.

- CloudButton Project: [http://cloudbutton.eu/](http://cloudbutton.eu/)
- CloudButton Toolkit: [https://github.com/cloudbutton/cloudbutton](https://github.com/cloudbutton/cloudbutton)

## Requirements

 - [pip](https://pypi.org/project/pip/) (updated)
 - aliyun-fc2 (`pip install aliyun-fc2`)
 - oss2 (`pip install oss2`)
 
## Plugin setup

If you have not installed `cloudbutton` yet, you first have to [install](https://github.com/cloudbutton/cloudbutton) it.\
Assuming you already have installed Cloudbutton:

  1. Clone this repository.
  2. Execute the `install_plugin.py` script. 
```
  python3 install_plugin.py
```
  3. Edit your local Cloudbutton config file (typically ~/.cloudbutton_config)
     with the new parameters for Aliyun.\
     See [config_tempate.yaml](/config_template.yaml)
```yaml
  aliyun_oss:
    public_endpoint : <PUBLIC_ENDPOINT>
    internal_endpoint : <INTRANET_ENDPOINT>
    access_key_id : <ACCESS_KEY_ID>
    access_key_secret : <ACCESS_KEY_SECRET>

  aliyun_fc:
    public_endpoint : <PUBLIC_ENDPOINT>
    access_key_id : <ACCESS_KEY_ID>
    access_key_secret : <ACCESS_KEY_SECRET>
```
   - `public_endpoint`: public endpoint (URL) to the service. OSS and FC endpoints are different.
   - `internal_endpoint`: internal endpoint (URL) to the service. Provides cost-free inbound and outbound traffic among services from the same intranet (region).
   - `access_key_id`: Access Key Id.
   - `access_key_secret`: Access Key Secret. 
      
      In addition, you have to specify a bucket that will be used internally by Cloudbutton, and you have indicate that you want Cloudbutton to use Aliyun OSS / FC:     
```yaml
  cloudbutton:
    storage_bucket : <BUCKET_NAME>
    storage_backend : aliyun_oss
    compute_backend : aliyun_fc
```
  4. Use the Cloudbutton toolkit in your Python code.


## Custom runtime
The Cloudbutton agent (handler) uses a default runtime with some common modules to run your code (see [requirements.txt](/compute/backends/aliyun_fc/requirements.txt)). However, if your code often requires a module that is not already included in the runtime, it will be convinient to build your custom runtime.\
The process is very simple. You only have to install your modules into a separate folder (via `pip install -t <CUSTOM_MODULES_DIR>`) and then provide it to Cloudbutton by specifing it in the config file:
```yaml
  cloudbutton:
    ...
    runtime : <CUSTOM_MODULES_DIR>
```
Or in your code:
```python
  pool = Pool(initargs={'runtime': '<CUSTOM_MODULES_DIR>'})
```

Note that the actual folder name in which you installed your modules will be used from now on to identify this runtime, thus after the first execution (which will install it to Aliyun FC) you can use that name to refer to it instead of the full path. For example, with */home/me/mycustomruntime* as the directory of your custom modules, you will be able to use *mycustomruntime* to refer to it:
```yaml
  cloudbutton:
    ...
    runtime : mycustomruntime
```
Or:
```python
  pool = Pool(initargs={'runtime': 'mycustomruntime'})
```

Finally, remember that Aliyun Function Compute has [limits](https://www.alibabacloud.com/help/doc-detail/51907.htm?spm=a2c63.l28256.b99.152.1dd43c94NMby9d) regarding runtimes.
