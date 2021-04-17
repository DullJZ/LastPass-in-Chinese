# LastPass-in-Chinese
# LastPass 汉化版
> 2021.4.17 更新：新增自动安装语言包功能，再也不用繁琐的复制粘贴了！

> 注意：现在LastPass已经把免费套餐改为移动端或电脑端二选一同步。也就是说，想要白嫖LastPass的电脑手机同步功能的可以下车了。
## 汉化原因

1. 原本 LastPass 是有中文的，然而 苏州智务采信息技术有限公司 恶意抢注了中国区 LastPass 的商标，借此勒索钱财，LastPass 被迫退出中国市场，也因此取消了对中文的支持。~~真是比马克丁还马克丁~~
2. 在网上找了两圈，发现有汉化解决方案，并提供了一个汉化的 `messages.json` 文件，然而实际使用后却错漏百出，不但直接一键替换所有相同单词，还把hide（隐藏）翻译为帮助（help），实在看不下去，决定自己翻译：<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/%E7%9B%B4%E6%8E%A5%E4%B8%80%E9%94%AE%E6%9B%BF%E6%8D%A2%E6%89%80%E6%9C%89%E7%9B%B8%E5%90%8C%E5%8D%95%E8%AF%8D.jpg" height="300" width="500">
    <br>
    <div style="color:orange; border-bottom: 1px solid #d9d9d9;
    display: inline-block;
    color: #999;
    padding: 2px;">直接一键替换所有相同单词</div>
</center>

## 汉化方法
>注意：每一次更新LastPass扩展都需要汉化一次！更新会自动覆盖语言包！
### 自动汉化（仅 Microsoft Edge 和 Google Chome）
下载 release 中的 `auto-install.exe` ，按照提示操作即可。
FireFox用户请看手动汉化流程

### 手动汉化
<details>
<summary>展开查看</summary>
<pre><code>

### Chromium 系浏览器
1. 下载该存储库的 `messages.json` 文件
2. 打开该路径：（以Edge Beta为例）

    >说明：bbcinlkgjjkejfdpemiealijmmooekmp 指的是浏览器扩展的ID，在这里查看 
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/ID.jpg)

    ```
    C:\Users\你的用户名\AppData\Local\Microsoft\Edge Beta\User Data\Default\Extensions\bbcinlkgjjkejfdpemiealijmmooekmp\4.64.0.3_0\_locales\en_US
    ```

    >当然也可以使用everything搜索浏览器扩展的ID
3. 重命名该目录下的 `messages.json` 为其他名称
4. 把下载的 `messages.json` 复制到该目录下
5. 重启浏览器即可

### Firefox 浏览器
1. 下载该存储库的 `messages.json` 文件
2. 打开该路径：
    
    ```
    C:\Users\你的用户名\AppData\Roaming\Mozilla\Firefox\Profiles\o41pb3hc.default-release\extensions
    ```
    >不知道不同版本是否有偏差，自己看着办
3. 打开 `support@lastpass.com.xpi`
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass0.jpg)
4. 重命名该目录下的 `messages.json` 为其他名称
5. 把下载的 `messages.json` 复制到该目录下
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass7.jpg)
6. 重启浏览器，发现新情况：
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass2.jpg)
7. 点击【了解详情】，发现解决方案：
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass3.jpg)
8. 去下载Firefox 开发者版 或Nightly版 （以开发者版为例）
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass4.jpg)![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass5.jpg)
9. 安装后在Firefox 开发者版中安装LastPass 扩展，并打开如下路径，打开 `support@lastpass.com.xpi`：
    ```
    C:\Users\你的用户名\AppData\Roaming\Mozilla\Firefox\Profiles\c6pq2wn8.dev-edition-default\extensions
    ```
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass6.jpg)
10. 重复操作4、5
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass1.jpg)
11. 按照【了解详情】中的解决方案操作
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass8.jpg)![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass9.jpg)
12. 重启浏览器，问题解决！:)
    ![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass10.jpg)![](https://cdn.jsdelivr.net/gh/jiangzhe11/MyPicture/Firefox%20last%20pass11.jpg)

</code></pre>
</details>

## 翻译问题
#### Note含有多个意思，如“笔记”、“注释”等，不予翻译，保留。
#### Vault被不同的人翻译为“金库”、“仓库”等，为避免歧义，保留。
#### Credit Monitoring 谷歌翻译为为“信用监控”，但我感觉应该是“信用卡监控”，网上搜索也找不到，还是按照谷歌翻译来。

## 注意
`messages.json` 一共近8000行，仅靠我一人不可能完全翻译完。我只汉化了一部分，也许还会不定期更新。欢迎大家 Pull Requests 提交翻译。