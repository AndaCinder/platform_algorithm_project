import requests
from flask import Flask, request, jsonify
import json
from entity.bean import CapabilityInfo, MyEncoder, ResultMsg, TaskInfo, ImagePart

app = Flask(__name__)


@app.route('/api/ads/v1/setup-addr', methods=['POST'])
def setup_addr():
    """设置服务地址接口"""
    params = request.get_data()
    if params is None or params == "":
        return jsonify("Parameter can not be empty.", status=403)
    # result_ip result_port license_ip license_port
    param_dict = json.loads(params)
    # 这里接受到参数再做运行
    # 生成返回值，目前先写死
    retval = ResultMsg(0, "success").__dict__
    return jsonify(retval)


@app.route("/api/ads/v1/resources", methods=['GET'])
def get_resources():
    """查询算法资源信息接口"""
    # 算法能力集信息
    capability_info = CapabilityInfo(0, 0, 16, 2)
    capa_info_serial = json.dumps(capability_info, cls=MyEncoder)
    retval = ResultMsg(0, "success").__dict__
    # 算法能力集信息，code 为 0 时必传
    retval["capability_info"] = capa_info_serial
    return jsonify(retval)


@app.route("/api/ads/v1/tasks", methods=['POST'])
def start_task():
    """创建并启动视频流分析任务
        1. 该接口用于创建并启动视频流算法分析，由第三方厂商提供的算法镜像服务 ADS实现提供。
        2. 可根据不同分析算法，制定可选的算法分析规则
        3. 任务创建后，ads 需注意更新资源能力使用情况及任务信息，华智会通过
            6.2查询算法资源信息接口(算法厂商提供实现)及 6.4 查询任务状态信息接口(算法厂商提供实现)接口查询能力情况及任务分析情况。
        4. ads 无须持久化任务数据
    """
    get4Req = request.get_data()
    if get4Req is None or get4Req == "":
        return jsonify("Parameter can not be empty.", status=403)
    # 这里如果得到的json不规范会报错
    params = json.loads(get4Req)
    # task_id stream_url analysis_rules(obj[]) private_data(obj)
    retval = ResultMsg(0, "success").__dict__
    retval["task_id"] = params["task_id"]
    return jsonify(retval)


@app.route("/api/ads/v1/task-status", methods=['GET'])
def query_task_status():
    """查询任务状态信息接口
    1. 该接口为算法镜像服务 ADS 提供的任务状态信息查询接口。
    2. 华智视图分析系统通过轮询该接口获取任务状态，实现任务的保活。
    """
    # task_info (obj[])
    retval = ResultMsg(0, "success").__dict__
    retval["task_info"] = []
    # 例如现在查到两个任务
    retval["task_info"].append(TaskInfo("xxx1", 0, "").__dict__)
    retval["task_info"].append(TaskInfo("xxx2", 0, "fetch rtsp failed").__dict__)
    return jsonify(retval)


@app.route("/api/ads/v1/task/<task_id>", methods=['DELETE'])
def stop_del_task(task_id):
    """停止并删除视频流分析任务"""
    retval = ResultMsg(0, "success").__dict__
    retval["task_id"] = task_id
    return jsonify(retval)


@app.route("/api/ads/v1/images-anlysis", methods=["POST"])
def images_analysis():
    """图片分析(json+base64)"""
    params = request.get_data()
    if params is None or params == "":
        return jsonify("Parameter can not be empty.", status=403)
    # {image_list:{image_id, image_type, data, url， analysis_rules， private_data}， sync}
    param_dict = json.loads(params)
    # 封装数据
    retval = ResultMsg(0, "success").__dict__
    result = []
    item = {"image_id": "xxx1", "result": result, "private_data": {}}
    img_part_list = [ImagePart(101, 89, 100, 200).__dict__]
    result.append({"attr_data": {"eventSort": 33892184}, "img_part_list": img_part_list})
    retval["data"] = []
    retval["data"].append(item)
    return jsonify(retval)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
