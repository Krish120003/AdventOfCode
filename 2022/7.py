# from pprint import pprint as print
from math import *
from itertools import *

# --- Day 7: No Space Left On Device ---
# You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?

# The device the Elves gave you has problems with more than just its communication system. You try to run a system update:

# $ system-update --please --pretty-please-with-sugar-on-top
# Error: No space left on device
# Perhaps you can delete some files to make space for the update?

# You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

# Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

# cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
# cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
# cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
# cd / switches the current directory to the outermost directory, /.
# ls means list. It prints out all of the files and directories immediately contained by the current directory:
# 123 abc means that the current directory contains a file named abc with size 123.
# dir xyz means that the current directory contains a directory named xyz.
# Given the commands and output in the example above, you can determine that the filesystem looks visually like this:

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
# Here, there are four directories: / (the outermost directory), a and d (which are in /), and e (which is in a). These directories also contain files of various sizes.

# Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the total size of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)

# The total sizes of the directories above can be found as follows:

# The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.
# The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
# Directory d has total size 24933642.
# As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
# To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

x = """
$ cd /
$ ls
dir gts
68377 jvdqjhr.jvp
dir lwhbw
228884 nqth.gcn
dir pcqjnl
94844 ppwv.zsh
97889 rqpw
dir sqhw
dir vllgn
dir wdtm
dir ztfdwp
$ cd gts
$ ls
846 grwwbrgz.wft
72000 mrnhn.psz
155241 qvnbd.dqs
6655 tndtmwfv
$ cd ..
$ cd lwhbw
$ ls
99946 lrrl.lth
$ cd ..
$ cd pcqjnl
$ ls
76420 gdg.lvr
dir gljcvm
161390 hlnrq.mjj
dir lqwntmdg
dir lrrl
dir qgpr
222006 tndtmwfv
$ cd gljcvm
$ ls
264381 tmwzlzn
$ cd ..
$ cd lqwntmdg
$ ls
dir jjfwr
dir rfqbmb
$ cd jjfwr
$ ls
dir cfhjvmh
$ cd cfhjvmh
$ ls
dir gzfgc
$ cd gzfgc
$ ls
134989 cfhjvmh.wwh
$ cd ..
$ cd ..
$ cd ..
$ cd rfqbmb
$ ls
dir cbrvhz
dir flcw
dir mnd
$ cd cbrvhz
$ ls
131072 wdtm.rjr
$ cd ..
$ cd flcw
$ ls
216675 wlfwpb.wpg
$ cd ..
$ cd mnd
$ ls
28976 hzzzzvmr.lsz
$ cd ..
$ cd ..
$ cd ..
$ cd lrrl
$ ls
dir cpmvnf
dir dcfmtw
dir ggnwqcj
7864 lgsc.smg
42042 mjfdjrgt
dir mrnhn
258288 nqth.gcn
dir nwjggvr
249578 qfnnncr.ftw
dir sqpgr
dir wgpqg
3196 wtpmdqhd.snd
$ cd cpmvnf
$ ls
dir srtqvcv
$ cd srtqvcv
$ ls
dir mrnhn
$ cd mrnhn
$ ls
dir fbrwd
$ cd fbrwd
$ ls
163166 nqth.gcn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd dcfmtw
$ ls
31712 mrnhn.tgg
dir nzpdtfr
dir sntcbctt
dir vzhvjp
dir wdtm
$ cd nzpdtfr
$ ls
dir qwtwps
130527 rhhlfg.tcj
160893 rwbwp.rmr
dir vcthd
$ cd qwtwps
$ ls
dir cmf
$ cd cmf
$ ls
73595 wdsjg.thm
$ cd ..
$ cd ..
$ cd vcthd
$ ls
15016 cfhjvmh
$ cd ..
$ cd ..
$ cd sntcbctt
$ ls
dir lrrl
dir mjfdjrgt
dir npqj
$ cd lrrl
$ ls
258433 clgfwbb.htg
166151 fbt.cnp
$ cd ..
$ cd mjfdjrgt
$ ls
64472 csphnrqr
222554 fbt.cnp
30487 vqb.grr
$ cd ..
$ cd npqj
$ ls
154071 mtn.pjq
185929 nqth.gcn
$ cd ..
$ cd ..
$ cd vzhvjp
$ ls
161341 mrnhn.wvw
$ cd ..
$ cd wdtm
$ ls
224565 cdd
dir jrswcjq
dir smgbdw
$ cd jrswcjq
$ ls
173122 blm.znb
$ cd ..
$ cd smgbdw
$ ls
307533 cfhjvmh.ppp
$ cd ..
$ cd ..
$ cd ..
$ cd ggnwqcj
$ ls
dir bfjvt
146815 fbt.cnp
279655 nljrr
152735 qpv
$ cd bfjvt
$ ls
193338 qlfcz
238188 qnz.llm
$ cd ..
$ cd ..
$ cd mrnhn
$ ls
dir cfhjvmh
dir cjsrvg
32604 fbt.cnp
231569 fpjfth.mmc
dir hghjzpgc
270425 mjfdjrgt.fdt
273944 mjfdjrgt.twj
141791 ztswsbs.pjs
$ cd cfhjvmh
$ ls
306620 lrrl.mgd
$ cd ..
$ cd cjsrvg
$ ls
303619 dffrqscq.nct
16738 lrrl.rbb
63842 zbbwj
$ cd ..
$ cd hghjzpgc
$ ls
dir mgnq
273152 mnszcbnv.fzj
$ cd mgnq
$ ls
dir ttmctqlc
250332 wdsjg.thm
20054 zpzml
$ cd ttmctqlc
$ ls
9006 nqth.gcn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd nwjggvr
$ ls
dir bwmglvmt
202937 lqqmqzl.vqj
dir lrrl
dir wmjp
dir zvlhngjm
$ cd bwmglvmt
$ ls
dir bszd
244726 dnwvnsn.npc
dir dqdrngf
226857 jvcn
dir lrrl
288079 mjfdjrgt.ttw
172669 vqr
dir wtqgd
$ cd bszd
$ ls
3937 csn.mft
198599 vpbccpm
$ cd ..
$ cd dqdrngf
$ ls
26680 lrrl.gch
150627 tndtmwfv
$ cd ..
$ cd lrrl
$ ls
dir bzrs
27874 grjbtv
$ cd bzrs
$ ls
71351 wlfwpb.wpg
$ cd ..
$ cd ..
$ cd wtqgd
$ ls
58033 lrrl.cgp
16732 vnznzhc.bzr
137407 wlfwpb.wpg
$ cd ..
$ cd ..
$ cd lrrl
$ ls
dir wrtp
$ cd wrtp
$ ls
267582 nwmj.rlb
$ cd ..
$ cd ..
$ cd wmjp
$ ls
155158 szhljp
dir tzqqmmp
163989 zwz.jvq
$ cd tzqqmmp
$ ls
140115 qgwcfnvr.fzt
$ cd ..
$ cd ..
$ cd zvlhngjm
$ ls
dir fjt
214803 mjfdjrgt.zrb
dir qsvwfb
187556 tcqgvqr.gmv
185730 tndtmwfv
301659 wlfwpb.wpg
$ cd fjt
$ ls
57947 mnchj
$ cd ..
$ cd qsvwfb
$ ls
23145 dzrgbhgf.dcm
$ cd ..
$ cd ..
$ cd ..
$ cd sqpgr
$ ls
dir bpnlrhsb
dir jvdh
dir zplwvj
$ cd bpnlrhsb
$ ls
22875 wdsjg.thm
$ cd ..
$ cd jvdh
$ ls
95461 ftmzfwt
$ cd ..
$ cd zplwvj
$ ls
dir gtd
$ cd gtd
$ ls
50675 lgjbhr.jmc
$ cd ..
$ cd ..
$ cd ..
$ cd wgpqg
$ ls
65679 wlfwpb.wpg
$ cd ..
$ cd ..
$ cd qgpr
$ ls
dir fhnnc
dir jzmpcc
dir lrrl
dir wdtm
$ cd fhnnc
$ ls
84726 tndtmwfv
$ cd ..
$ cd jzmpcc
$ ls
dir mjfdjrgt
dir mrnhn
dir wdtm
120156 whz.cts
134435 wlfwpb.wpg
$ cd mjfdjrgt
$ ls
234188 wdtm.bpt
$ cd ..
$ cd mrnhn
$ ls
dir gphqmvpn
dir gvtgqn
$ cd gphqmvpn
$ ls
23807 nzl.hzv
$ cd ..
$ cd gvtgqn
$ ls
225267 fbt.cnp
132455 mrnhn.vcn
$ cd ..
$ cd ..
$ cd wdtm
$ ls
dir cfhjvmh
dir mjfdjrgt
119601 mjfdjrgt.rhc
226225 wdsjg.thm
191042 wdtm
$ cd cfhjvmh
$ ls
130491 dgdcbwqp.czm
$ cd ..
$ cd mjfdjrgt
$ ls
87408 djd.ccj
152868 mjfdjrgt.zcn
22605 srdfwwtj.rcp
$ cd ..
$ cd ..
$ cd ..
$ cd lrrl
$ ls
26548 zwrctnn.lln
$ cd ..
$ cd wdtm
$ ls
dir jszntstc
$ cd jszntstc
$ ls
210953 gwgmnvsh.nhb
277302 msqjtrdm
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd sqhw
$ ls
dir djw
dir dqnhzbh
dir lwp
dir mjfdjrgt
211273 mjfdjrgt.hls
dir mrnhn
$ cd djw
$ ls
98290 cfhjvmh.jpr
$ cd ..
$ cd dqnhzbh
$ ls
43311 bdf.pzd
68801 cfwdq.rbz
dir cmfhw
dir cwtm
77978 nnzhntgh
138343 nqth.gcn
81692 tzhltsq
dir zwhs
$ cd cmfhw
$ ls
dir dsbjlmrf
215307 fbt.cnp
dir lch
217372 mjfdjrgt.dzq
228751 tndtmwfv
dir tpgszv
$ cd dsbjlmrf
$ ls
92510 pzq.hcl
$ cd ..
$ cd lch
$ ls
171339 czhsjn.ttq
$ cd ..
$ cd tpgszv
$ ls
215263 nvgcfqzb.gww
$ cd ..
$ cd ..
$ cd cwtm
$ ls
105200 twrb.ljq
$ cd ..
$ cd zwhs
$ ls
35576 gnt.zdh
68204 mfg
207974 njb.lzw
$ cd ..
$ cd ..
$ cd lwp
$ ls
65175 jcwncw.tms
208506 tndtmwfv
$ cd ..
$ cd mjfdjrgt
$ ls
dir hlgqdqb
153252 mjfdjrgt.njp
dir pdsdjdlz
144949 phsnm.bvl
287686 zlszpmlv.gsf
$ cd hlgqdqb
$ ls
128570 fdbls
dir lmhrtp
dir mjfdjrgt
184639 mjfdjrgt.lct
168706 mmlfd
159454 mrdljff
dir pzcnzs
dir rcmzfm
86088 tndtmwfv
$ cd lmhrtp
$ ls
251922 cfhjvmh.njw
$ cd ..
$ cd mjfdjrgt
$ ls
61866 nqtrmm.zts
24980 wlfwpb.wpg
$ cd ..
$ cd pzcnzs
$ ls
123265 fbt.cnp
$ cd ..
$ cd rcmzfm
$ ls
dir gjls
$ cd gjls
$ ls
109021 cnzz
$ cd ..
$ cd ..
$ cd ..
$ cd pdsdjdlz
$ ls
103346 zhfhrzmr.qqm
$ cd ..
$ cd ..
$ cd mrnhn
$ ls
dir tmldr
140361 tndtmwfv
$ cd tmldr
$ ls
169607 dvchnsqr.ltc
$ cd ..
$ cd ..
$ cd ..
$ cd vllgn
$ ls
58389 tndtmwfv
$ cd ..
$ cd wdtm
$ ls
dir cfhjvmh
dir cpcqz
dir gmrgsmpp
290978 jbfn
179525 mjfdjrgt
dir mrnhn
dir nvgmrpdf
dir vpm
67780 wlfwpb.wpg
dir ztp
$ cd cfhjvmh
$ ls
dir hqf
218467 lfl.vpp
dir rgq
147778 rhntpj
dir tgmw
$ cd hqf
$ ls
207656 blvtl.zhg
$ cd ..
$ cd rgq
$ ls
54691 cfhjvmh.mhw
201230 jjhr.lml
22759 mgqdg.qsj
$ cd ..
$ cd tgmw
$ ls
153570 nqth.gcn
$ cd ..
$ cd ..
$ cd cpcqz
$ ls
dir cfhjvmh
17143 fbt.cnp
dir ftpm
dir lrrl
92760 lwdzptgw.gfv
dir mrnhn
151636 tndtmwfv
dir vqt
$ cd cfhjvmh
$ ls
17554 wlfwpb.wpg
$ cd ..
$ cd ftpm
$ ls
244476 crpfc.bwn
290894 dhdnh
210196 lhf
58166 nqth.gcn
$ cd ..
$ cd lrrl
$ ls
229894 btrbfh.twr
269093 cfhjvmh.pbb
277722 fvhtjpg.pvb
236232 gztc.lbh
dir mjfdjrgt
230753 qgjrh.zsf
dir sdvhlnz
$ cd mjfdjrgt
$ ls
186105 lrrl.zng
226081 lsdzz.gsj
33416 nqth.gcn
109966 wgtclbvt.nct
160015 wlfwpb.wpg
$ cd ..
$ cd sdvhlnz
$ ls
219905 cngbvwz.zsm
284092 dgjz
dir lcmlmr
22135 lrrl
dir vdcbcvzv
dir wdwgp
dir zllqgnhj
$ cd lcmlmr
$ ls
dir lrrl
$ cd lrrl
$ ls
104034 cpv
$ cd ..
$ cd ..
$ cd vdcbcvzv
$ ls
263858 qwsmpvdv.lfr
dir sldsnqld
$ cd sldsnqld
$ ls
3116 hvsb.vrj
166766 wqfg.ztg
$ cd ..
$ cd ..
$ cd wdwgp
$ ls
11714 wdsjg.thm
$ cd ..
$ cd zllqgnhj
$ ls
113285 hrjtqzvf
$ cd ..
$ cd ..
$ cd ..
$ cd mrnhn
$ ls
212363 bhldtsnn.jbp
194936 wdsjg.thm
$ cd ..
$ cd vqt
$ ls
46371 lrrl.ztz
215875 rnggjsg.hsw
255959 vnjhm.frz
277765 vwvjnrjp.mwq
$ cd ..
$ cd ..
$ cd gmrgsmpp
$ ls
dir fbcv
275639 fbt.cnp
dir tnrmj
65119 vtfjqtw.tqg
117334 zsg.grj
$ cd fbcv
$ ls
dir htmwl
292840 wwwspsb.hrb
$ cd htmwl
$ ls
34803 dshcw
10573 dwtd
$ cd ..
$ cd ..
$ cd tnrmj
$ ls
dir cfhjvmh
dir wqtnrwg
$ cd cfhjvmh
$ ls
110464 wlfwpb.wpg
$ cd ..
$ cd wqtnrwg
$ ls
283055 mfgllgv
$ cd ..
$ cd ..
$ cd ..
$ cd mrnhn
$ ls
2633 tndtmwfv
$ cd ..
$ cd nvgmrpdf
$ ls
32919 pnc
$ cd ..
$ cd vpm
$ ls
dir ddz
dir dhmphrn
dir grr
132419 mgfdgw.vlt
dir nbccdd
dir plw
183717 pvgbbjgt.wbt
dir qsmg
120729 stbh.rvz
101652 ttqc
$ cd ddz
$ ls
4672 hrnnrzd
217020 wdtm
$ cd ..
$ cd dhmphrn
$ ls
dir fwbmb
dir gdq
dir lrrl
dir mrcnm
dir mrmmr
161427 rllvrpzl.vcg
$ cd fwbmb
$ ls
258937 dfd.wrl
103543 gtfgscfg.jjc
$ cd ..
$ cd gdq
$ ls
133691 bzgt.llh
278010 cfhjvmh.nhj
191344 cjbcnfz.rjb
269115 fbt.cnp
$ cd ..
$ cd lrrl
$ ls
dir gqqsg
dir gwbtt
dir mrnhn
140500 nqth.gcn
dir pdtm
220764 tndtmwfv
dir vvsvfchb
$ cd gqqsg
$ ls
dir gvn
dir hzfmdhw
34666 vfzbvl
dir wdtm
$ cd gvn
$ ls
206457 cfhjvmh.thh
133435 hsdsstt
dir lrrl
dir rwvbmlq
127003 sjqvt.lzl
136402 wlfwpb.wpg
60537 zwjfrqf.nvl
$ cd lrrl
$ ls
15291 mrnhn.ltr
190429 wlfwpb.wpg
119328 wln.msz
86384 zbhzvrc.gbj
$ cd ..
$ cd rwvbmlq
$ ls
186907 nqth.gcn
$ cd ..
$ cd ..
$ cd hzfmdhw
$ ls
9653 fbt.cnp
dir lvdhtg
301280 nqth.gcn
dir nwnp
241354 vzrbbj.bfb
$ cd lvdhtg
$ ls
dir cfhjvmh
dir hzpzz
296694 mjfdjrgt.mpj
65800 nqth.gcn
dir pbfhn
dir wljjgs
$ cd cfhjvmh
$ ls
87654 htlq
203005 vhmthzjb
$ cd ..
$ cd hzpzz
$ ls
153446 brfstm.nwc
47585 cfhjvmh
258754 wdtm.gpt
150809 zlwq.hgr
$ cd ..
$ cd pbfhn
$ ls
dir mjfdjrgt
$ cd mjfdjrgt
$ ls
16108 rmfwpm.fnt
$ cd ..
$ cd ..
$ cd wljjgs
$ ls
228757 bqf.jll
$ cd ..
$ cd ..
$ cd nwnp
$ ls
124842 lrrl
$ cd ..
$ cd ..
$ cd wdtm
$ ls
122771 fbt.cnp
252697 lpqf.bvg
264813 mrnhn
165228 pgn.wnw
dir vsls
292567 wlfwpb.wpg
$ cd vsls
$ ls
250070 dvbv
$ cd ..
$ cd ..
$ cd ..
$ cd gwbtt
$ ls
dir mjfdjrgt
2327 nqth.gcn
20064 sdjvgv.sfr
$ cd mjfdjrgt
$ ls
96726 fbt.cnp
4801 lrrl.fgv
180291 wspcp.brw
$ cd ..
$ cd ..
$ cd mrnhn
$ ls
dir lrrl
dir mqcstf
271459 nqth.gcn
190006 zdln
$ cd lrrl
$ ls
160260 fbt.cnp
281732 tfpprjj
$ cd ..
$ cd mqcstf
$ ls
222125 gntrdss.zcw
dir pdbbbmn
58613 stwlp.wpl
$ cd pdbbbmn
$ ls
250947 mjfdjrgt
$ cd ..
$ cd ..
$ cd ..
$ cd pdtm
$ ls
55975 wdhn
$ cd ..
$ cd vvsvfchb
$ ls
10547 hpwmnjgc
157960 tcc
$ cd ..
$ cd ..
$ cd mrcnm
$ ls
106708 cfhjvmh
264809 ffqfm.slz
dir lrrl
dir mjfdjrgt
174610 wlfwpb.wpg
90207 wwhwvdc.zvc
$ cd lrrl
$ ls
305034 fbt.cnp
240756 jmfwlmzv.gjc
77875 wgfpcscz.mdn
$ cd ..
$ cd mjfdjrgt
$ ls
26073 mrnhn
$ cd ..
$ cd ..
$ cd mrmmr
$ ls
287663 qlc
$ cd ..
$ cd ..
$ cd grr
$ ls
dir tgb
$ cd tgb
$ ls
203808 psssw.nzs
$ cd ..
$ cd ..
$ cd nbccdd
$ ls
62162 wfmhzh
$ cd ..
$ cd plw
$ ls
185632 ljwvnppm.bcc
$ cd ..
$ cd qsmg
$ ls
164538 lrrl.flr
dir vbvtzmsg
dir wrrtctvd
$ cd vbvtzmsg
$ ls
15318 mrnhn.qlh
$ cd ..
$ cd wrrtctvd
$ ls
249219 lggjwn.mfj
$ cd ..
$ cd ..
$ cd ..
$ cd ztp
$ ls
241178 fzc.swf
dir hns
223340 lbmzvf
dir wdtm
195144 wlfwpb.wpg
$ cd hns
$ ls
dir fshzss
77792 mjfdjrgt.qcm
85013 nlpsw
274710 pmclgp.lvz
dir spdzjs
$ cd fshzss
$ ls
297058 fbj.qjm
131320 wjbhllz.mnf
$ cd ..
$ cd spdzjs
$ ls
165766 nrzthq.rvj
10584 zfhqhm.njj
$ cd ..
$ cd ..
$ cd wdtm
$ ls
dir vnmg
$ cd vnmg
$ ls
83938 mrnhn.wwd
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ztfdwp
$ ls
152895 swjdzqdh.ngv
215804 tndtmwfv
68954 wdsjg.thm
"""

# x = """
# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""

data = x.strip().split("\n")[1:]

# use nested lists to represent the filesystem
# each list is a directory
# each item in the list is a file or directory
# each file is a tuple of (name, size)
# each directory is a tuple of (name, list)
# the filesystem is the root directory at /


class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = {}
        self.parent = None

    def add(self, item):
        self.contents[item.name] = item
        item.parent = self

    def size(self):
        return sum(item.size() for item in self.contents.values())

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Directory({self.name})"


class File:
    def __init__(self, name, size):
        self.name = name
        self.sz = int(size)
        self.parent = None

    def size(self):
        return self.sz

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"File({self.name}, {self.sz})"


filesystem = Directory("/")

currentDir = filesystem
cursor = 0
while cursor < len(data):
    try:
        line = data[cursor]
    except IndexError:
        break

    if line.startswith("$ ls"):
        while True:
            cursor += 1
            try:
                line = data[cursor]
            except IndexError:
                break

            if line.startswith("$"):
                break

            if line.startswith("dir"):
                currentDir.add(Directory(line[4:]))
            else:
                filesize, filename = line.split(" ")
                currentDir.add(File(filename, filesize))

    elif line.startswith("$ cd"):

        if line.startswith("$ cd /"):
            currentDir = filesystem

        elif line.startswith("$ cd .."):
            currentDir = currentDir.parent

        elif line.startswith("$ cd "):
            # create the directory if it doesn't exist
            if line[5:] not in currentDir.contents:
                currentDir.add(Directory(line[5:]))
            currentDir = currentDir.contents[line[5:]]

        cursor += 1


# function to print the filesystem
def printfs(fs, indent=0):
    for item in fs.contents.values():
        print(" " * indent, item)
        if isinstance(item, Directory):
            printfs(item, indent + 2)


printfs(filesystem)
# print(filesystem.contents)

# find all directories with size <= 100000


def find_small_dirs(fs, size=100000):
    result = []
    for item in fs.contents.values():
        if isinstance(item, Directory):
            if item.size() <= size:
                result.append(item)
            result.extend(find_small_dirs(item, size))
    return result


print(sum(e.size() for e in find_small_dirs(filesystem)))

# PART 2
# Now, you're ready to choose a directory to delete.

# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

# In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

# To achieve this, you have the following options:

# Delete directory e, which would increase unused space by 584.
# Delete directory a, which would increase unused space by 94853.
# Delete directory d, which would increase unused space by 24933642.
# Delete directory /, which would increase unused space by 48381165.
# Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?


# find free space
free_space = 70000000 - filesystem.size()
to_free_up = 30000000 - free_space

# find all directories with size >= to_free_up


def find_big_dirs(fs, size):
    result = set()

    if fs.size() >= size:
        result.add(fs)
    for item in fs.contents.values():
        if isinstance(item, Directory):
            if item.size() >= size:
                result.add(item)
            result.update(find_big_dirs(item, size))
    return result


a = find_big_dirs(filesystem, to_free_up)

# find smallest in a
a = min(a, key=lambda x: x.size())


print(a.size())
print(filesystem.size(), to_free_up)
