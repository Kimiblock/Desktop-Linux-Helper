# 监测独立显卡活动

------

![Screenshot_20220910_204102](https://github.com/Kimiblock/Desktop-Linux-Helper/raw/master/GPUMonitor/Screenshot_20220910_204102.png)

![Screenshot_20220910_204102](https://github.com/Kimiblock/Desktop-Linux-Helper/raw/master/GPUMonitor/D3Cold.png)

本脚本能在笔记本独立显卡启动 (从 `D3cold` 状态切换其他状态)时发送桌面通知, 支持 `Ampere` 及之后的 N卡, A卡理论上支持.

目前看来 `Chromium` 类应用启动时总是会触发一次, 申明 `Vulkan` 显卡和 flag 指定显卡均无效

默认监测 `card1`, 可以更改环境变量 `${cardNumber}`

# 使用

创建一个 `.desktop` 文件开机启动

# 依赖

`Breeze` 图标主题, `notify-send`

