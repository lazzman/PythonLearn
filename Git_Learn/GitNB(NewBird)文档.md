# 1.Git的介绍
> Git是目前世界上最先进的分布式版本控制系统。

# 2.Git与SVN的区别
> SVN是集中式版本控制系统，版本库是集中放在中央服务器的，而干活的时候，用的都是自己的电脑，所以首先要从中央服务器哪里得到最新的版本，然后干活， 干完后，需要把自己做完的活推送到中央服务器。集中式版本控制系统是必须联网才能工作，如果在局域网还可以，带宽够大，速度够快，如果在互联网下，如果网 速慢的话，就纳闷了。

> Git是分布式版本控制系统，那么它就没有中央服务器的，每个人的电脑就是一个完整的版本库，这样，工作的时候就不需要联网了，因为版本都是在自己的电脑 上。既然每个人的电脑都有一个完整的版本库，那多个人如何协作呢？比如说自己在电脑上改了文件A，其他人也在电脑上改了文件A，这时，你们两之间只需把各 自的修改推送给对方，就可以互相看到对方的修改了。

# 3.windows安装教程
> - 下载msysgit
- 默认安装即可
- 安装完成后打开开始菜单中"Git –> Git Bash"，如下:
> ![](http://static.open-open.com/lib/uploadImg/20141027/20141027155917_719.jpg)
> - 弹出Git Bash黑窗口，输入git version 成功看到git版本信息说明可以正常使用了

# 4.windows安装Git完成后必须注意的设置
> ![](http://static.open-open.com/lib/uploadImg/20141027/20141027155918_624.jpg)
> 　　注意：git config  –global 参数，有了这个参数，表示你这台机器上所有的Git仓库都会使用这个配置，当然你也可以对某个仓库指定的不同的用户名和邮箱。
> 　　当我们初始化一个仓库后，.git目录下的config文件存储了我们的配置信息，例如github仓库的url。

# 5.开始使用
> #### 一：创建版本库
>     什么是版本库？版本库又名仓库，英文名repository,你可以简单的理解一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改，删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻还可以将文件"还原"。

> **这里分两种情况：**

> - 在本地创建版本库
- 在github上创建版本库

> `1.初始化版本库。如果在github上新建版本库，新建完成后进入项目主页，这样就完成了github的版本库初始操作；如果是本地创建版本库，需要新建一个项目目录，打开当前目录的输入git init，这样就把本地的这个文件夹变为了git版本库，会发现这个文件夹下多了一个隐藏的.git文件夹，这个目录很重要！不要随手删掉啊！！！`

> `2.把文件添加到版本库中。首先要明确下，所有的版本控制系统，只能跟踪文本文件的改动，比如txt文件，网页，所有程序的代码等，Git也不列外，版本控制系统可以告诉你每次的改 动，但是图片，视频这些二进制文件，虽能也能由版本控制系统管理，但没法跟踪文件的变化，只能把二进制文件每次改动串起来，也就是知道图片从1kb变成 2kb，但是到底改了啥，版本控制也不知道。`
　　**下面先看下demo如下演示：**

>> 　　我们已经初始化了一个版本库，如图所示：
![初始化后的版本库](http://upload-images.jianshu.io/upload_images/4191539-44e2690768b27882.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
** 第一步：使用命令` git add readme.txt`添加到暂存区里面去。如下：**
![git add命令](http://upload-images.jianshu.io/upload_images/4191539-2997a7053d7d68c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　如果和上面一样，没有任何提示，说明已经添加成功了。
** 第二步：用命令` git commit`告诉Git，把文件提交到仓库。**
![git commit命令](http://upload-images.jianshu.io/upload_images/4191539-7e61725581f85357.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
** 第三步：现在我们已经提交了一个readme.txt文件了，我们下面可以通过命令` git status`来查看是否还有文件未提交，如下：**
![git status命令](http://upload-images.jianshu.io/upload_images/4191539-451dd6ff2e94096b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　说明没有任何文件未提交，但是我现在继续来改下readme.txt内容，比如我在下面添加一行2222222222内容，继续使用` git status`来查看下结果，如下：
![git status命令](http://upload-images.jianshu.io/upload_images/4191539-4bd7b8058c79309f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　上面的命令告诉我们 readme.txt文件已被修改，但是未被提交的修改。
接下来我想看下readme.txt文件到底改了什么内容，如何查看呢？
* 可以使用如下命令：` git diff readme.txt`如下：
![git diff命令](http://upload-images.jianshu.io/upload_images/4191539-d05ecd900ef67ad0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　如上可以看到，readme.txt文件内容从一行11111111改成 二行 添加了一行22222222内容。
　　知道了对readme.txt文件做了什么修改后，我们可以放心的提交到仓库了，提交修改和提交文件是一样的2步(第一步是` git add ` 第二步是：` git commit`)。如下：
![git commit命令](http://upload-images.jianshu.io/upload_images/4191539-da488156c3a7df86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> #### 二：版本回退
>> 　　如上，我们已经学会了修改文件，现在我继续对readme.txt文件进行修改，再增加一行内容为33333333333333.继续执行命令如下：
![git add 与 git commit命令](http://upload-images.jianshu.io/upload_images/4191539-f18ed29c27bb3666.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　现在我已经对readme.txt文件做了三次修改了，那么我现在想查看下历史记录，如何查呢？
　　我们现在可以使用命令` git log`演示如下所示：
![git log命令](http://upload-images.jianshu.io/upload_images/4191539-d34d82411ae2abd1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　git log命令显示从最近到最远的显示日志，我们可以看到最近三次提交，最近的一次是,增加内容为333333.上一次是添加内容222222，第一次默认是 111111.如果嫌上面显示的信息太多的话，我们可以使用命令` git log –pretty=oneline `演示如下：
![git log命令](http://upload-images.jianshu.io/upload_images/4191539-8cb2764921730271.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　现在我想使用版本回退操作，我想把当前的版本回退到上一个版本，要使用什么命令呢？可以使用如下2种命令，第一种是：` git reset  --hard HEAD^ `那么如果要回退到上上个版本只需把HEAD^ 改成 HEAD^^ 以此类推。那如果要回退到前100个版本的话，使用上面的方法肯定不方便，我们可以使用下面的简便命令操作：` git reset  --hard HEAD~100` 即可。未回退之前的readme.txt内容如下：
![未回退之前的内容](http://upload-images.jianshu.io/upload_images/4191539-4af6c1c044395e4f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　如果想回退到上一个版本的命令如下操作：
![git reset命令](http://upload-images.jianshu.io/upload_images/4191539-7f8a52967d0d90f4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　再来查看下 readme.txt内容如下：通过命令cat readme.txt查看
![查看回退后的内容](http://upload-images.jianshu.io/upload_images/4191539-937a8e3d4787d008.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　可以看到，内容已经回退到上一个版本了。我们可以继续使用` git log`来查看下历史记录信息，如下：
![git log命令](http://upload-images.jianshu.io/upload_images/4191539-410cd44e25282534.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　我们看到 增加333333 内容我们没有看到了，但是现在我想回退到最新的版本，如：有333333的内容要如何恢复呢？我们可以通过版本号回退，使用命令方法如下：
 ` git reset --hard 版本号`，但是现在的问题假如我已经关掉过一次命令行或者333内容的版本号我并不知道呢？要如何知道增加3333内容的版本号呢？
　　可以通过如下命令即可获取到版本号：` git reflog` 演示如下：
![get reflog命令](http://upload-images.jianshu.io/upload_images/4191539-b8edee165623250f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
通过上面的显示我们可以知道，增加内容3333的版本号是 6fcfc89.我们现在可以命令
* ` git reset --hard 6fcfc89`来恢复了。演示如下：
![git reset --hard 版本号](http://upload-images.jianshu.io/upload_images/4191539-d43c79f0318b6b87.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　可以看到，目前已经是最新的版本了。

> #### 三：理解工作区与暂存区的区别？
>> * ** 工作区：**
　　就是你在电脑上看到的目录，比如目录下testgit里的文件(.git隐藏目录版本库除外)。或者以后需要再新建的目录文件等等都属于工作区范畴。
* ** 版本库(Repository)：**
　　工作区有一个隐藏目录.git,这个不属于工作区，这是版本库。其中版本库里面存了很多东西，其中最重要的就是stage(暂存区)，还有Git为我们自动创建了第一个分支master,以及指向master的一个指针HEAD。
我们前面说过使用Git提交文件到版本库有两步：
　　第一步：是使用 git add 把文件添加进去，实际上就是把文件添加到暂存区。
　　第二步：使用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支上。
我们继续使用demo来演示下：
　　我们在readme.txt再添加一行内容为4444444，接着在目录下新建一个文件为test.txt 内容为test，我们先用命令` git status`来查看下状态，如下： 
![git status](http://upload-images.jianshu.io/upload_images/4191539-e89a6b58eaf46104.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　现在我们先使用` git add`命令把2个文件都添加到暂存区中，再使用` git status`来查看下状态，如下： 
![git status](http://upload-images.jianshu.io/upload_images/4191539-7363880d0efc57e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　接着我们可以使用` git commit`一次性提交到分支上，如下： 
![git commit](http://upload-images.jianshu.io/upload_images/4191539-15c0914c2c003aee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> #### 四：Git撤销修改和删除文件操作
>> ** 一：撤销修改：**
　　比如我现在在readme.txt文件里面增加一行 内容为555555555555，我们先通过命令查看如下： 
![查看文本内容](http://upload-images.jianshu.io/upload_images/4191539-261e127dc6913bba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　在我未提交之前，我发现添加5555555555555内容有误，所以我得马上恢复以前的版本，现在我可以有如下几种方法可以做修改：
　　第一：如果我知道要删掉那些内容的话，直接手动更改去掉那些需要的文件，然后add添加到暂存区，最后commit掉。
　　第二：我可以按以前的方法直接恢复到上一个版本。使用` git reset --hard HEAD^`，但是现在我不想使用上面的2种方法，我想直接想使用撤销命令该如何操作呢？首先在做撤销之前，我们可以先用` git status `查看下当前的状态。如下所示： 
![git status命令](http://upload-images.jianshu.io/upload_images/4191539-11aa0d226ecc9ed2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　可以发现，Git会告诉你，` git checkout  -- file`可以丢弃工作区的修改，如下命令：` git checkout -- readme.txt`，如下所示： 
![git check](http://upload-images.jianshu.io/upload_images/4191539-a24e41c3a8e1c898.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　命令` git checkout –readme.txt `意思就是，把readme.txt文件在工作区做的修改全部撤销，这里有2种情况，如下：
　　1. readme.txt自动修改后，还没有放到暂存区，使用 撤销修改就回到和版本库一模一样的状态。
　　2. 另外一种是readme.txt已经放入暂存区了，接着又作了修改，撤销修改就回到添加暂存区后的状态。
　　对于第二种情况，我想我们继续做demo来看下，假如现在我对readme.txt添加一行 内容为6666666666666，我` git add`增加到暂存区后，接着添加内容7777777，我想通过撤销命令让其回到暂存区后的状态。如下所示： 
![Demo](http://upload-images.jianshu.io/upload_images/4191539-8ff20122afbc8037.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>> **注意：**命令` git checkout -- readme.txt `中的 -- 很重要，如果没有 -- 的话，那么命令变成创建分支了。
>> **二：删除文件：**
　　假如我现在版本库testgit目录添加一个文件b.txt,然后提交。如下： 
![Demo](http://upload-images.jianshu.io/upload_images/4191539-c5e63da409fd66d1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　如上：一般情况下，可以直接在文件目录中把文件删了，或者使用如上rm命令：rm b.txt ，如果我想彻底从版本库中删掉了此文件的话，可以再执行commit命令 提交掉，现在目录是这样的：
![当前目录](http://upload-images.jianshu.io/upload_images/4191539-b91ffa78e2ad8080.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　只要没有commit之前，如果我想在版本库中恢复此文件如何操作呢？
可以使用如下命令` git checkout -- b.txt`，如下所示： 
![git check -- fileName](http://upload-images.jianshu.io/upload_images/4191539-c1f2cfddd93e82e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　再来看看我们testgit目录，添加了3个文件了。如下所示： 
![当前目录](http://upload-images.jianshu.io/upload_images/4191539-3fc94fc52383803d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> #### 五：远程仓库
在了解之前，先注册github账号，github支持两种链接方式，一种https方式，另一种是ssh方式。
** HTTPS方式：这种方式比较简单粗暴，但是并不安全。**
![https方式](http://upload-images.jianshu.io/upload_images/4191539-303ee2d5e47439ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
** SSH方式：你的本地Git仓库和github仓库之间的传输是通过SSH加密的，所以需要先进行设置：**
　　第一步：创建SSH Key。在用户主目录下，看看有没有.ssh目录，如果有，再看看这个目录下有没有id_rsa和id_rsa.pub这两个文件，如果有的话，直接跳过此如下命令，如果没有的话，打开git-bash，输入如下命令：` ssh -keygen -t rsa –C "youremail@example.com"`, 由于我本地此前运行过一次，所以本地有，如下所示：
![生成ssh key](http://upload-images.jianshu.io/upload_images/4191539-8febf8456c8e44b4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
* 　　id_rsa是私钥，不能泄露出去，id_rsa.pub是公钥，可以放心地告诉任何人* 
　　第二步：登录github,打开” settings”中的SSH Keys页面，然后点击“Add SSH Key”,填上任意title，在Key文本框里黏贴id_rsa.pub文件的内容。
![Github配置](http://upload-images.jianshu.io/upload_images/4191539-3fea719469ba4544.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　点击 Add Key，你就应该可以看到已经添加的key。
![Github配置](http://upload-images.jianshu.io/upload_images/4191539-f20cec151ad9088e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
>> ** 1.添加远程库：**
　　现在的情景是：我们已经在本地创建了一个Git仓库后，又想在github创建一个Git仓库，并且希望这两个仓库进行远程同步，这样github的仓库可以作为备份，又可以其他人通过该仓库来协作。
　　首先，登录github上，然后在右上角找到“create a new repo”创建一个新的仓库。如下： 
![Github](http://upload-images.jianshu.io/upload_images/4191539-2ac66bca42e2dce5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　在Repository name填入testgit，其他保持默认设置，点击“Create repository”按钮，就成功地创建了一个新的Git仓库：
![github](http://upload-images.jianshu.io/upload_images/4191539-b15adcb2cb98c89f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　目前，在GitHub上的这个testgit仓库还是空的，GitHub告诉我们，可以从这个仓库克隆出新的仓库，也可以把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。
　　现在，我们根据GitHub的提示，在本地的testgit仓库下运行命令：
` git remote add origin https://github.com/tugenhua0707/testgit.git`
　　如下所示： 
![将本地版本库与Github远程库关联](http://upload-images.jianshu.io/upload_images/4191539-32b29b5e7b253112.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　把本地库的内容推送到远程，使用` git push`命令，实际上是把当前分支master推送到远程。
　　由于远程库是空的，我们第一次推送master分支时，加上了 –u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来， 在以后的推送或者拉取时就可以简化命令。推送成功后，可以立刻在github页面中看到远程库的内容已经和本地一模一样了，上面的要输入github的用 户名和密码如下所示： 
![git push](http://upload-images.jianshu.io/upload_images/4191539-9f620964e5bc3b18.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
　　从现在起，只要本地作了提交，就可以通过如下命令：
` git push origin master`
把本地master分支的最新修改推送到github上了，现在你就拥有了真正的分布式版本库了。
>> ** 2.从远程库克隆：**
上面我们了解了先有本地库，后有远程库时候，如何关联远程库。
现在我们想，假如远程库有新的内容了，我想克隆到本地来 如何克隆呢？
首先，登录github，创建一个新的仓库，名字叫testgit2.如下： 





