# 1.Git的介绍
> Git是目前世界上最先进的分布式版本控制系统。

# 2.Git与SVN的区别
> SVN是集中式版本控制系统，版本库是集中放在中央服务器的，而干活的时候，用的都是自己的电脑，所以首先要从中央服务器哪里得到最新的版本，然后干活， 干完后，需要把自己做完的活推送到中央服务器。集中式版本控制系统是必须联网才能工作，如果在局域网还可以，带宽够大，速度够快，如果在互联网下，如果网 速慢的话，就纳闷了。

> Git是分布式版本控制系统，那么它就没有中央服务器的，每个人的电脑就是一个完整的版本库，这样，工作的时候就不需要联网了，因为版本都是在自己的电脑 上。既然每个人的电脑都有一个完整的版本库，那多个人如何协作呢？比如说自己在电脑上改了文件A，其他人也在电脑上改了文件A，这时，你们两之间只需把各 自的修改推送给对方，就可以互相看到对方的修改了。

# 3.windows安装教程
- 下载msysgit
- 默认安装即可
- 安装完成后打开开始菜单中"Git –> Git Bash"，如下:

![](http://static.open-open.com/lib/uploadImg/20141027/20141027155917_719.jpg)

- 弹出Git Bash黑窗口，输入git version 成功看到git版本信息说明可以正常使用了

# 4.windows安装Git完成后必须注意的设置
![](http://static.open-open.com/lib/uploadImg/20141027/20141027155918_624.jpg)
> 注意：git config  –global 参数，有了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然你也可以对某个仓库指定的不同的用户名和邮箱。

> 当我们初始化一个仓库后，.git目录下的config文件存储了我们的配置信息，例如github仓库的url。

# 5.开始使用
> #### 一.创建版本库
>     什么是版本库？版本库又名仓库，英文名repository,你可以简单的理解一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改，删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻还可以将文件"还原"。

> **这里分两种情况：**

> - 在本地创建版本库
- 在github上创建版本库

> `1.初始化版本库。如果在github上新建版本库，新建完成后进入项目主页，这样就完成了github的版本库初始操作；如果是本地创建版本库，需要新建一个项目目录，打开当前目录的输入git init，这样就把本地的这个文件夹变为了git版本库，会发现这个文件夹下多了一个隐藏的.git文件夹，这个目录很重要！不要随手删掉啊！！！`

> `2.把文件添加到版本库中。首先要明确下，所有的版本控制系统，只能跟踪文本文件的改动，比如txt文件，网页，所有程序的代码等，Git也不列外，版本控制系统可以告诉你每次的改 动，但是图片，视频这些二进制文件，虽能也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是知道图片从1kb变成 2kb，但是到底改了啥，版本控制也不知道。`
**下面先看下** **demo** **如下演示：**
>> 我们已经初始化了一个版本库，如图所示：
![初始化后的版本库](http://upload-images.jianshu.io/upload_images/4191539-44e2690768b27882.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
`* 第一步：使用命令 git add readme.txt添加到暂存区里面去。如下：`
![git add命令](http://upload-images.jianshu.io/upload_images/4191539-2997a7053d7d68c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
如果和上面一样，没有任何提示，说明已经添加成功了。
`* 第二步：用命令 git commit告诉Git，把文件提交到仓库。`
![git commit命令](http://upload-images.jianshu.io/upload_images/4191539-7e61725581f85357.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
`* 第三步：现在我们已经提交了一个readme.txt文件了，我们下面可以通过命令git status来查看是否还有文件未提交，如下：`
![git status命令](http://upload-images.jianshu.io/upload_images/4191539-451dd6ff2e94096b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
说明没有任何文件未提交，但是我现在继续来改下readme.txt内容，比如我在下面添加一行2222222222内容，继续使用git status来查看下结果，如下：
![git status命令](http://upload-images.jianshu.io/upload_images/4191539-4bd7b8058c79309f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
上面的命令告诉我们 readme.txt文件已被修改，但是未被提交的修改。
接下来我想看下readme.txt文件到底改了什么内容，如何查看呢？
`* 可以使用如下命令：git diff readme.txt 如下：`
![git diff命令](http://upload-images.jianshu.io/upload_images/4191539-d05ecd900ef67ad0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
如上可以看到，readme.txt文件内容从一行11111111改成 二行 添加了一行22222222内容。
知道了对readme.txt文件做了什么修改后，我们可以放心的提交到仓库了，提交修改和提交文件是一样的2步(第一步是git add  第二步是：git commit)。
如下：
![git commit命令](http://upload-images.jianshu.io/upload_images/4191539-da488156c3a7df86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> #### 二.版本回退
>> 如上，我们已经学会了修改文件，现在我继续对readme.txt文件进行修改，再增加一行内容为33333333333333.继续执行命令如下：
![git add 与 git commit命令](http://upload-images.jianshu.io/upload_images/4191539-f18ed29c27bb3666.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
现在我已经对readme.txt文件做了三次修改了，那么我现在想查看下历史记录，如何查呢？
`我们现在可以使用命令 git log 演示如下所示：`
![git log命令](http://upload-images.jianshu.io/upload_images/4191539-d34d82411ae2abd1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
git log命令显示从最近到最远的显示日志，我们可以看到最近三次提交，最近的一次是,增加内容为333333.上一次是添加内容222222，第一次默认是 111111.如果嫌上面显示的信息太多的话，我们可以使用命令 git log –pretty=oneline 演示如下：
![git log命令](http://upload-images.jianshu.io/upload_images/4191539-8cb2764921730271.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
`现在我想使用版本回退操作，我想把当前的版本回退到上一个版本，要使用什么命令呢？可以使用如下2种命令，第一种是：git reset  –hard HEAD^ 那么如果要回退到上上个版本只需把HEAD^ 改成 HEAD^^ 以此类推。那如果要回退到前100个版本的话，使用上面的方法肯定不方便，我们可以使用下面的简便命令操作：git reset  –hard HEAD~100 即可。`未回退之前的readme.txt内容如下：
![未回退之前的内容](http://upload-images.jianshu.io/upload_images/4191539-4af6c1c044395e4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
如果想回退到上一个版本的命令如下操作：
![git reset命令](http://upload-images.jianshu.io/upload_images/4191539-7f8a52967d0d90f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
再来查看下 readme.txt内容如下：通过命令cat readme.txt查看
![查看回退后的内容](http://upload-images.jianshu.io/upload_images/4191539-937a8e3d4787d008.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
可以看到，内容已经回退到上一个版本了。我们可以继续使用git log 来查看下历史记录信息，如下：
![git log命令](http://upload-images.jianshu.io/upload_images/4191539-410cd44e25282534.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我们看到 增加333333 内容我们没有看到了，但是现在我想回退到最新的版本，如：有333333的内容要如何恢复呢？`我们可以通过版本号回退，使用命令方法如下：
git reset  –hard 版本号 ，但是现在的问题假如我已经关掉过一次命令行或者333内容的版本号我并不知道呢？要如何知道增加3333内容的版本号呢？可以通过如下命令即可获取到版本号：git reflog ` 
演示如下：
