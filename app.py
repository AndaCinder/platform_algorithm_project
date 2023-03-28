import requests
from flask import Flask, request, jsonify
import json
from entity.bean import CapabilityInfo, MyEncoder

app = Flask(__name__)


@app.route('/api/ads/v1/setup-addr', methods=['POST'])
def setup_addr():
    """设置服务地址接口"""
    params = request.get_data()
    if params is None or params == "":
        return jsonify("Parameter set_config can not be empty.", status=403)
    # result_ip result_port license_ip license_port
    param_dict = json.loads(params)
    # 这里接受到参数再做运行
    # 生成返回值，目前先写死
    retval = {"code": 0, "error_msg": "success"}
    return jsonify(retval)


@app.route("/api/ads/v1/resources", methods=['GET'])
def get_resources():
    """查询算法资源信息接口"""
    # 算法能力集信息
    capability_info = CapabilityInfo(0, 0, 16, 2)
    capa_info_serial = json.dumps(capability_info, cls=MyEncoder)
    retval = {
        "code": 0,  # 0 表示查询成功，非 0 表示其他错误
        "error_msg": "success",  # 错误信息描述，成功填写"success"
        "capability_info": capa_info_serial  # 算法能力集信息，code 为 0 时必传
    }
    return jsonify(retval)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
