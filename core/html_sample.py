'''
=================================================
@Author ：Andy
@Date   ：2020/7/10 18:12
==================================================
'''

BRUSH_INDEX = '''
            <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <!-- custom CSS -->
    <link href="../core/resources/css/main.css" rel="stylesheet" type="text/css"/>
    <script type="text/javascript" src="../core/resources/assets/echarts.min.js"></script>
    <title>Home</title>
</head>
<body>
<!-- Header -->
<header id="header" class="header">
    <div class="header_down container wrapper clearfix bigmegamenu">
        <!--Main Menu HTML Code-->
        <nav class="wsmenu slideLeft clearfix">
            <ul class="mobile-sub wsmenu-list">
                <li class="active">
                    <span class="wsmenu-click"></span>
                    <a href="">综合指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/综合指数/上证指数.html">上证指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/Ａ股指数.html">Ａ股指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/B股指数.html">B股指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/工业指数.html">工业指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/商业指数.html">商业指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/地产指数.html">地产指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/公用指数.html">公用指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/综合指数.html">综合指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/新综指.html">新综指</a></li>
                        <li><a href="plot_kline_brush/综合指数/中型综指.html">中型综指</a></li>
                        <li><a href="plot_kline_brush/综合指数/上证流通.html">上证流通</a></li>
                        <li><a href="plot_kline_brush/综合指数/新 指 数.html">新 指 数</a></li>
                        <li><a href="plot_kline_brush/综合指数/中小板综.html">中小板综</a></li>
                        <li><a href="plot_kline_brush/综合指数/创业板综.html">创业板综</a></li>
                        <li><a href="plot_kline_brush/综合指数/深证综指.html">深证综指</a></li>
                        <li><a href="plot_kline_brush/综合指数/深证A指.html">深证A指</a></li>
                        <li><a href="plot_kline_brush/综合指数/深证B指.html">深证B指</a></li>
                        <li><a href="plot_kline_brush/综合指数/农林指数.html">农林指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/采矿指数.html">采矿指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/制造指数.html">制造指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/水电指数.html">水电指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/建筑指数.html">建筑指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/批零指数.html">批零指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/运输指数.html">运输指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/住宿餐饮指数.html">住宿餐饮指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/IT指数.html">IT指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/金融指数.html">金融指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/地产指数.html">地产指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/商务指数.html">商务指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/科研指数.html">科研指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/公共指数.html">公共指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/文化指数.html">文化指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/综企指数.html">综企指数</a></li>
                        <li><a href="plot_kline_brush/综合指数/国证Ａ指.html">国证Ａ指</a></li>
                        <li><a href="plot_kline_brush/综合指数/国证Ｂ指.html">国证Ｂ指</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">基金指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/基金指数/基金指数.html">基金指数</a></li>
                        <li><a href="plot_kline_brush/基金指数/乐富指数.html">乐富指数</a></li>
                        <li><a href="plot_kline_brush/基金指数/基金指数.html">基金指数</a></li>
                        <li><a href="plot_kline_brush/基金指数/深证ETF.html">深证ETF</a></li>
                        <li><a href="plot_kline_brush/基金指数/国证基金.html">国证基金</a></li>
                        <li><a href="plot_kline_brush/基金指数/国证ETF.html">国证ETF</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">债券指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/债券指数/国债指数.html">国债指数</a></li>
                        <li><a href="plot_kline_brush/债券指数/企债指数.html">企债指数</a></li>
                        <li><a href="plot_kline_brush/债券指数/沪公司债.html">沪公司债</a></li>
                        <li><a href="plot_kline_brush/债券指数/沪企债30.html">沪企债30</a></li>
                        <li><a href="plot_kline_brush/债券指数/5年信用.html">5年信用</a></li>
                        <li><a href="plot_kline_brush/债券指数/信用100.html">信用100</a></li>
                        <li><a href="plot_kline_brush/债券指数/上证转债.html">上证转债</a></li>
                        <li><a href="plot_kline_brush/债券指数/中证转债.html">中证转债</a></li>
                        <li><a href="plot_kline_brush/债券指数/中高企债.html">中高企债</a></li>
                        <li><a href="plot_kline_brush/债券指数/深信中高.html">深信中高</a></li>
                        <li><a href="plot_kline_brush/债券指数/深信中低.html">深信中低</a></li>
                        <li><a href="plot_kline_brush/债券指数/深信用债.html">深信用债</a></li>
                        <li><a href="plot_kline_brush/债券指数/深公司债.html">深公司债</a></li>
                        <li><a href="plot_kline_brush/债券指数/深证转债.html">深证转债</a></li>
                        <li><a href="plot_kline_brush/债券指数/深证转债.html">深证转债</a></li>
                        <li><a href="plot_kline_brush/债券指数/企债指数.html">企债指数</a></li>
                        <li><a href="plot_kline_brush/债券指数/公司债指.html">公司债指</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">价值指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/价值指数/180价值.html">180价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/180R价值.html">180R价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/全指价值.html">全指价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/全R价值.html">全R价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/380价值.html">380价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/380R价值.html">380R价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/300价值.html">300价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/深证价值.html">深证价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/国证价值.html">国证价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/大盘价值.html">大盘价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/中盘价值.html">中盘价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/小盘价值.html">小盘价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/中小价值.html">中小价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/中创价值.html">中创价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/700价值.html">700价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/1000价值.html">1000价值</a></li>
                        <li><a href="plot_kline_brush/价值指数/创业板V.html">创业板V</a></li>
                        <li><a href="plot_kline_brush/价值指数/300 价值.html">300 价值</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">规模指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/规模指数/上证380.html">上证380</a></li>
                        <li><a href="plot_kline_brush/规模指数/上证180.html">上证180</a></li>
                        <li><a href="plot_kline_brush/规模指数/上证50.html">上证50</a></li>
                        <li><a href="plot_kline_brush/规模指数/超大盘.html">超大盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/上证中盘.html">上证中盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/上证小盘.html">上证小盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/上证中小.html">上证中小</a></li>
                        <li><a href="plot_kline_brush/规模指数/上证全指.html">上证全指</a></li>
                        <li><a href="plot_kline_brush/规模指数/市值百强.html">市值百强</a></li>
                        <li><a href="plot_kline_brush/规模指数/沪深300.html">沪深300</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证1000.html">中证1000</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证100.html">中证100</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证200.html">中证200</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证500.html">中证500</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证800.html">中证800</a></li>
                        <li><a href="plot_kline_brush/规模指数/两岸三地.html">两岸三地</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证成指.html">深证成指</a></li>
                        <li><a href="plot_kline_brush/规模指数/深成指R.html">深成指R</a></li>
                        <li><a href="plot_kline_brush/规模指数/成份Ｂ指.html">成份Ｂ指</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证100R.html">深证100R</a></li>
                        <li><a href="plot_kline_brush/规模指数/中小板指.html">中小板指</a></li>
                        <li><a href="plot_kline_brush/规模指数/创业板指.html">创业板指</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证300.html">深证300</a></li>
                        <li><a href="plot_kline_brush/规模指数/中小300.html">中小300</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证200.html">深证200</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证700.html">深证700</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证1000.html">深证1000</a></li>
                        <li><a href="plot_kline_brush/规模指数/创业300.html">创业300</a></li>
                        <li><a href="plot_kline_brush/规模指数/中小创新.html">中小创新</a></li>
                        <li><a href="plot_kline_brush/规模指数/沪深300.html">沪深300</a></li>
                        <li><a href="plot_kline_brush/规模指数/国证2000.html">国证2000</a></li>
                        <li><a href="plot_kline_brush/规模指数/国证50.html">国证50</a></li>
                        <li><a href="plot_kline_brush/规模指数/国证1000.html">国证1000</a></li>
                        <li><a href="plot_kline_brush/规模指数/国证300.html">国证300</a></li>
                        <li><a href="plot_kline_brush/规模指数/综企指巨潮100.html">综企指巨潮100</a></li>
                        <li><a href="plot_kline_brush/规模指数/巨潮大盘.html">巨潮大盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/巨潮中盘.html">巨潮中盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/巨潮小盘.html">巨潮小盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证100.html">深证100</a></li>
                        <li><a href="plot_kline_brush/规模指数/中小板R.html">中小板R</a></li>
                        <li><a href="plot_kline_brush/规模指数/深证300R.html">深证300R</a></li>
                        <li><a href="plot_kline_brush/规模指数/大中盘.html">大中盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/中小盘.html">中小盘</a></li>
                        <li><a href="plot_kline_brush/规模指数/创业板R.html">创业板R</a></li>
                        <li><a href="plot_kline_brush/规模指数/中创100R.html">中创100R</a></li>
                        <li><a href="plot_kline_brush/规模指数/中创100.html">中创100</a></li>
                        <li><a href="plot_kline_brush/规模指数/中小基础.html">中小基础</a></li>
                        <li><a href="plot_kline_brush/规模指数/中创400.html">中创400</a></li>
                        <li><a href="plot_kline_brush/规模指数/中创500.html">中创500</a></li>
                        <li><a href="plot_kline_brush/规模指数/创业基础.html">创业基础</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证100.html">中证100</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证 200.html">中证 200</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证 500.html">中证 500</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证 700.html">中证 700</a></li>
                        <li><a href="plot_kline_brush/规模指数/中证超大.html">中证超大</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">成长指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/成长指数/180成长.html">180成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/180R成长.html">180R成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/全指成长.html">全指成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/全R成长.html">全R成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/380成长.html">380成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/380R成长.html">380R成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/300成长.html">300成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/深证成长.html">深证成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/国证成长.html">国证成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/大盘成长.html">大盘成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/中盘成长.html">中盘成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/小盘成长.html">小盘成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/中小成长.html">中小成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/中创成长.html">中创成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/700成长.html">700成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/1000成长.html">1000成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/创业板G.html">创业板G</a></li>
                        <li><a href="plot_kline_brush/成长指数/300 成长.html">300 成长</a></li>
                        <li><a href="plot_kline_brush/成长指数/300R成长.html">300R成长</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">策略指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/策略指数/50等权.html">50等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/180等权.html">180等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/50基本.html">50基本</a></li>
                        <li><a href="plot_kline_brush/策略指数/180基本.html">180基本</a></li>
                        <li><a href="plot_kline_brush/策略指数/能源等权.html">能源等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/材料等权.html">材料等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/工业等权.html">工业等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/可选等权.html">可选等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/消费等权.html">消费等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/医药等权.html">医药等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/金融等权.html">金融等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/信息等权.html">信息等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/电信等权.html">电信等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/公用等权.html">公用等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/180分层.html">180分层</a></li>
                        <li><a href="plot_kline_brush/策略指数/上证F200.html">上证F200</a></li>
                        <li><a href="plot_kline_brush/策略指数/上证F300.html">上证F300</a></li>
                        <li><a href="plot_kline_brush/策略指数/上证F500.html">上证F500</a></li>
                        <li><a href="plot_kline_brush/策略指数/380等权.html">380等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/380基本.html">380基本</a></li>
                        <li><a href="plot_kline_brush/策略指数/180波动.html">180波动</a></li>
                        <li><a href="plot_kline_brush/策略指数/380波动.html">380波动</a></li>
                        <li><a href="plot_kline_brush/策略指数/180高贝.html">180高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/180低贝.html">180低贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/380高贝.html">380高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/380低贝.html">380低贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/300高贝.html">300高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/800等权.html">800等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/基本面50.html">基本面50</a></li>
                        <li><a href="plot_kline_brush/策略指数/基本400.html">基本400</a></li>
                        <li><a href="plot_kline_brush/策略指数/等权90.html">等权90</a></li>
                        <li><a href="plot_kline_brush/策略指数/500等权.html">500等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/300等权.html">300等权</a></li>
                        <li><a href="plot_kline_brush/策略指数/百发100.html">百发100</a></li>
                        <li><a href="plot_kline_brush/策略指数/大盘低波.html">大盘低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/大盘高贝.html">大盘高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/中盘低波.html">中盘低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/中盘高贝.html">中盘高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/小盘低波.html">小盘低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/小盘高贝.html">小盘高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/红利100.html">红利100</a></li>
                        <li><a href="plot_kline_brush/策略指数/专利领先.html">专利领先</a></li>
                        <li><a href="plot_kline_brush/策略指数/深100EW.html">深100EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/深300EW.html">深300EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/中小板EW.html">中小板EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/创业板EW.html">创业板EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/100低波.html">100低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/深证绩效.html">深证绩效</a></li>
                        <li><a href="plot_kline_brush/策略指数/100绩效.html">100绩效</a></li>
                        <li><a href="plot_kline_brush/策略指数/300绩效.html">300绩效</a></li>
                        <li><a href="plot_kline_brush/策略指数/中小绩效.html">中小绩效</a></li>
                        <li><a href="plot_kline_brush/策略指数/深成指EW.html">深成指EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/中创EW.html">中创EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/深证低波.html">深证低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/深证高贝.html">深证高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/中小低波.html">中小低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/中小高贝.html">中小高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/中创低波.html">中创低波</a></li>
                        <li><a href="plot_kline_brush/策略指数/中创高贝.html">中创高贝</a></li>
                        <li><a href="plot_kline_brush/策略指数/深红利50.html">深红利50</a></li>
                        <li><a href="plot_kline_brush/策略指数/创业板50.html">创业板50</a></li>
                        <li><a href="plot_kline_brush/策略指数/深医药EW.html">深医药EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/深互联EW.html">深互联EW</a></li>
                        <li><a href="plot_kline_brush/策略指数/深证F60.html">深证F60</a></li>
                        <li><a href="plot_kline_brush/策略指数/深证F120.html">深证F120</a></li>
                        <li><a href="plot_kline_brush/策略指数/深证F200.html">深证F200</a></li>
                        <li><a href="plot_kline_brush/策略指数/基本面50.html">基本面50</a></li>
                        <li><a href="plot_kline_brush/策略指数/500等权.html">500等权</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">主题指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/主题指数/红利指数.html">红利指数</a></li>
                        <li><a href="plot_kline_brush/主题指数/180金融.html">180金融</a></li>
                        <li><a href="plot_kline_brush/主题指数/治理指数.html">治理指数</a></li>
                        <li><a href="plot_kline_brush/主题指数/180治理.html">180治理</a></li>
                        <li><a href="plot_kline_brush/主题指数/180基建.html">180基建</a></li>
                        <li><a href="plot_kline_brush/主题指数/180资源.html">180资源</a></li>
                        <li><a href="plot_kline_brush/主题指数/180运输.html">180运输</a></li>
                        <li><a href="plot_kline_brush/主题指数/180R价值.html">180R价值</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证央企.html">上证央企</a></li>
                        <li><a href="plot_kline_brush/主题指数/责任指数.html">责任指数</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证民企.html">上证民企</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证地企.html">上证地企</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证国企.html">上证国企</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证沪企.html">上证沪企</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证周期.html">上证周期</a></li>
                        <li><a href="plot_kline_brush/主题指数/非周期.html">非周期</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证龙头.html">上证龙头</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证商品.html">上证商品</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证新兴.html">上证新兴</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证资源.html">上证资源</a></li>
                        <li><a href="plot_kline_brush/主题指数/消费80.html">消费80</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪财中小.html">沪财中小</a></li>
                        <li><a href="plot_kline_brush/主题指数/资源50.html">资源50</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证上游.html">上证上游</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证中游.html">上证中游</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证下游.html">上证下游</a></li>
                        <li><a href="plot_kline_brush/主题指数/高端装备.html">高端装备</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪投资品.html">沪投资品</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪消费品.html">沪消费品</a></li>
                        <li><a href="plot_kline_brush/主题指数/持续产业.html">持续产业</a></li>
                        <li><a href="plot_kline_brush/主题指数/医药主题.html">医药主题</a></li>
                        <li><a href="plot_kline_brush/主题指数/农业主题.html">农业主题</a></li>
                        <li><a href="plot_kline_brush/主题指数/180动态.html">180动态</a></li>
                        <li><a href="plot_kline_brush/主题指数/180稳定.html">180稳定</a></li>
                        <li><a href="plot_kline_brush/主题指数/消费50.html">消费50</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证高新.html">上证高新</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证100.html">上证100</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证150.html">上证150</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证银行.html">上证银行</a></li>
                        <li><a href="plot_kline_brush/主题指数/380动态.html">380动态</a></li>
                        <li><a href="plot_kline_brush/主题指数/380稳定.html">380稳定</a></li>
                        <li><a href="plot_kline_brush/主题指数/优势资源.html">优势资源</a></li>
                        <li><a href="plot_kline_brush/主题指数/优势制造.html">优势制造</a></li>
                        <li><a href="plot_kline_brush/主题指数/优势消费.html">优势消费</a></li>
                        <li><a href="plot_kline_brush/主题指数/消费领先.html">消费领先</a></li>
                        <li><a href="plot_kline_brush/主题指数/180红利.html">180红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/380红利.html">380红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/上国红利.html">上国红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/上央红利.html">上央红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/上民红利.html">上民红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/上证环保.html">上证环保</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪股通.html">沪股通</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪新丝路.html">沪新丝路</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪中国造.html">沪中国造</a></li>
                        <li><a href="plot_kline_brush/主题指数/沪互联+.html">沪互联+</a></li>
                        <li><a href="plot_kline_brush/主题指数/500沪市.html">500沪市</a></li>
                        <li><a href="plot_kline_brush/主题指数/A股资源.html">A股资源</a></li>
                        <li><a href="plot_kline_brush/主题指数/消费服务.html">消费服务</a></li>
                        <li><a href="plot_kline_brush/主题指数/食品饮料.html">食品饮料</a></li>
                        <li><a href="plot_kline_brush/主题指数/医药生物.html">医药生物</a></li>
                        <li><a href="plot_kline_brush/主题指数/细分医药.html">细分医药</a></li>
                        <li><a href="plot_kline_brush/主题指数/细分地产.html">细分地产</a></li>
                        <li><a href="plot_kline_brush/主题指数/兴证海峡.html">兴证海峡</a></li>
                        <li><a href="plot_kline_brush/主题指数/有色金属.html">有色金属</a></li>
                        <li><a href="plot_kline_brush/主题指数/300红利.html">300红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/800有色.html">800有色</a></li>
                        <li><a href="plot_kline_brush/主题指数/中证环保.html">中证环保</a></li>
                        <li><a href="plot_kline_brush/主题指数/ESG 100.html">ESG 100</a></li>
                        <li><a href="plot_kline_brush/主题指数/300非银.html">300非银</a></li>
                        <li><a href="plot_kline_brush/主题指数/300有色.html">300有色</a></li>
                        <li><a href="plot_kline_brush/主题指数/央视500.html">央视500</a></li>
                        <li><a href="plot_kline_brush/主题指数/小康指数.html">小康指数</a></li>
                        <li><a href="plot_kline_brush/主题指数/中证红利.html">中证红利</a></li>
                        <li><a href="plot_kline_brush/主题指数/民企200.html">民企200</a></li>
                        <li><a href="plot_kline_brush/主题指数/财富大盘.html">财富大盘</a></li>
                        <li><a href="plot_kline_brush/主题指数/内地资源.html">内地资源</a></li>
                        <li><a href="plot_kline_brush/主题指数/300基建.html">300基建</a></li>
                        <li><a href="plot_kline_brush/主题指数/创业成长.html">创业成长</a></li>
                        <li><a href="plot_kline_brush/主题指数/银河99.html">银河99</a></li>
                        <li><a href="plot_kline_brush/主题指数/中证上游.html">中证上游</a></li>
                        <li><a href="plot_kline_brush/主题指数/中证下游.html">中证下游</a></li>
                        <li><a href="plot_kline_brush/主题指数/中证新兴.html">中证新兴</a></li>
                        <li><a href="plot_kline_brush/主题指数/300非周.html">300非周</a></li>
                        <li><a href="plot_kline_brush/主题指数/技术领先.html">技术领先</a></li>
                        <li><a href="plot_kline_brush/主题指数/800金融.html">800金融</a></li>
                        <li><a href="plot_kline_brush/主题指数/钱江30.html">钱江30</a></li>
                        <li><a href="plot_kline_brush/主题指数/新华金牛.html">新华金牛</a></li>
                        <li><a href="plot_kline_brush/主题指数/内地低碳.html">内地低碳</a></li>
                        <li><a href="plot_kline_brush/主题指数/医药100.html">医药100</a></li>
                        <li><a href="plot_kline_brush/主题指数/大宗商品.html">大宗商品</a></li>
                        <li><a href="plot_kline_brush/主题指数/智能资产.html">智能资产</a></li>
                        <li><a href="plot_kline_brush/主题指数/领先行业.html">领先行业</a></li>
                        <li><a href="plot_kline_brush/主题指数/大消费.html">大消费</a></li>
                        <li><a href="plot_kline_brush/主题指数/中证TMT.html">中证TMT</a></li>
                        <li><a href="plot_kline_brush/主题指数/深市精选.html">深市精选</a></li>
                        <li><a href="plot_kline_brush/主题指数/资源优势.html">资源优势</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">一级行业指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/一级行业指数/上证能源.html">上证能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证材料.html">上证材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证工业.html">上证工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证可选.html">上证可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证消费.html">上证消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证医药.html">上证医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证金融.html">上证金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证信息.html">上证信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证电信.html">上证电信</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/上证公用.html">上证公用</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380能源.html">380能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380材料.html">380材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380工业.html">380工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380可选.html">380可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380消费.html">380消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380医药.html">380医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380金融.html">380金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380信息.html">380信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380电信.html">380电信</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/380公用.html">380公用</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300能源.html">300能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300材料.html">300材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300工业.html">300工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300可选.html">300可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300消费.html">300消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300医药.html">300医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300金融.html">300金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300公用.html">300公用</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证能源.html">中证能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证可选.html">中证可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证消费.html">中证消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证金融.html">中证金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证信息.html">中证信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指能源.html">全指能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指材料.html">全指材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指可选.html">全指可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指消费.html">全指消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指医药.html">全指医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指金融.html">全指金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/全指信息.html">全指信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000能源.html">1000能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000材料.html">1000材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000工业.html">1000工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000可选.html">1000可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000消费.html">1000消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000医药.html">1000医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000金融.html">1000金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000信息.html">1000信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证通信.html">国证通信</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/1000公用.html">1000公用</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证银行.html">国证银行</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证汽车.html">国证汽车</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证交运.html">国证交运</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证传媒.html">国证传媒</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证农牧.html">国证农牧</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证煤炭.html">国证煤炭</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证证券.html">国证证券</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证电力.html">国证电力</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证油气.html">国证油气</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/国证钢铁.html">国证钢铁</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证能源.html">深证能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证材料.html">深证材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证工业.html">深证工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证可选.html">深证可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证消费.html">深证消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证医药.html">深证医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证金融.html">深证金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证信息.html">深证信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证电信.html">深证电信</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深证公用.html">深证公用</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深A医药.html">深A医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/深互联网.html">深互联网</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 能源.html">300 能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 材料.html">300 材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 工业.html">300 工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 可选.html">300 可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 消费.html">300 消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 医药.html">300 医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 金融.html">300 金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 信息.html">300 信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 电信.html">300 电信</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/300 公用.html">300 公用</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证能源.html">中证能源</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证材料.html">中证材料</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证工业.html">中证工业</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证可选.html">中证可选</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证消费.html">中证消费</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证金融.html">中证金融</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证信息.html">中证信息</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证电信.html">中证电信</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="plot_kline_brush/一级行业指数/基建工程.html">基建工程</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">二级行业指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_brush/二级行业指数/800医药.html">800医药</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/500原料.html">500原料</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/500工业.html">500工业</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/500医药.html">500医药</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/500信息.html">500信息</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/300银行.html">300银行</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/300地产.html">300地产</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/300运输.html">300运输</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/300银行.html">300银行</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/300地产.html">300地产</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/300运输.html">300运输</a></li>
                        <li><a href="plot_kline_brush/二级行业指数/800地产.html">800地产</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    </div>
</header>
</body>
</html>
'''

CHART_INDEX = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <!-- custom CSS -->
    <link href="../core/resources/css/main.css" rel="stylesheet" type="text/css"/>
    <script type="text/javascript" src="../core/resources/assets/echarts.min.js"></script>
    <title>Home</title>
</head>
<body>
<!-- Header -->
<header id="header" class="header">
    <div class="header_down container wrapper clearfix bigmegamenu">
        <!--Main Menu HTML Code-->
        <nav class="wsmenu slideLeft clearfix">
            <ul class="mobile-sub wsmenu-list">
                <li class="active">
                    <span class="wsmenu-click"></span>
                    <a href="">综合指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/综合指数/上证指数.html">上证指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/Ａ股指数.html">Ａ股指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/B股指数.html">B股指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/工业指数.html">工业指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/商业指数.html">商业指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/地产指数.html">地产指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/公用指数.html">公用指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/综合指数.html">综合指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/新综指.html">新综指</a></li>
                        <li><a href="plot_kline_chart/综合指数/中型综指.html">中型综指</a></li>
                        <li><a href="plot_kline_chart/综合指数/上证流通.html">上证流通</a></li>
                        <li><a href="plot_kline_chart/综合指数/新 指 数.html">新 指 数</a></li>
                        <li><a href="plot_kline_chart/综合指数/中小板综.html">中小板综</a></li>
                        <li><a href="plot_kline_chart/综合指数/创业板综.html">创业板综</a></li>
                        <li><a href="plot_kline_chart/综合指数/深证综指.html">深证综指</a></li>
                        <li><a href="plot_kline_chart/综合指数/深证A指.html">深证A指</a></li>
                        <li><a href="plot_kline_chart/综合指数/深证B指.html">深证B指</a></li>
                        <li><a href="plot_kline_chart/综合指数/农林指数.html">农林指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/采矿指数.html">采矿指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/制造指数.html">制造指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/水电指数.html">水电指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/建筑指数.html">建筑指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/批零指数.html">批零指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/运输指数.html">运输指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/住宿餐饮指数.html">住宿餐饮指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/IT指数.html">IT指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/金融指数.html">金融指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/地产指数.html">地产指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/商务指数.html">商务指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/科研指数.html">科研指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/公共指数.html">公共指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/文化指数.html">文化指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/综企指数.html">综企指数</a></li>
                        <li><a href="plot_kline_chart/综合指数/国证Ａ指.html">国证Ａ指</a></li>
                        <li><a href="plot_kline_chart/综合指数/国证Ｂ指.html">国证Ｂ指</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">基金指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/基金指数/基金指数.html">基金指数</a></li>
                        <li><a href="plot_kline_chart/基金指数/乐富指数.html">乐富指数</a></li>
                        <li><a href="plot_kline_chart/基金指数/基金指数.html">基金指数</a></li>
                        <li><a href="plot_kline_chart/基金指数/深证ETF.html">深证ETF</a></li>
                        <li><a href="plot_kline_chart/基金指数/国证基金.html">国证基金</a></li>
                        <li><a href="plot_kline_chart/基金指数/国证ETF.html">国证ETF</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">债券指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/债券指数/国债指数.html">国债指数</a></li>
                        <li><a href="plot_kline_chart/债券指数/企债指数.html">企债指数</a></li>
                        <li><a href="plot_kline_chart/债券指数/沪公司债.html">沪公司债</a></li>
                        <li><a href="plot_kline_chart/债券指数/沪企债30.html">沪企债30</a></li>
                        <li><a href="plot_kline_chart/债券指数/5年信用.html">5年信用</a></li>
                        <li><a href="plot_kline_chart/债券指数/信用100.html">信用100</a></li>
                        <li><a href="plot_kline_chart/债券指数/上证转债.html">上证转债</a></li>
                        <li><a href="plot_kline_chart/债券指数/中证转债.html">中证转债</a></li>
                        <li><a href="plot_kline_chart/债券指数/中高企债.html">中高企债</a></li>
                        <li><a href="plot_kline_chart/债券指数/深信中高.html">深信中高</a></li>
                        <li><a href="plot_kline_chart/债券指数/深信中低.html">深信中低</a></li>
                        <li><a href="plot_kline_chart/债券指数/深信用债.html">深信用债</a></li>
                        <li><a href="plot_kline_chart/债券指数/深公司债.html">深公司债</a></li>
                        <li><a href="plot_kline_chart/债券指数/深证转债.html">深证转债</a></li>
                        <li><a href="plot_kline_chart/债券指数/深证转债.html">深证转债</a></li>
                        <li><a href="plot_kline_chart/债券指数/企债指数.html">企债指数</a></li>
                        <li><a href="plot_kline_chart/债券指数/公司债指.html">公司债指</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">价值指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/价值指数/180价值.html">180价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/180R价值.html">180R价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/全指价值.html">全指价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/全R价值.html">全R价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/380价值.html">380价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/380R价值.html">380R价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/300价值.html">300价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/深证价值.html">深证价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/国证价值.html">国证价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/大盘价值.html">大盘价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/中盘价值.html">中盘价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/小盘价值.html">小盘价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/中小价值.html">中小价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/中创价值.html">中创价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/700价值.html">700价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/1000价值.html">1000价值</a></li>
                        <li><a href="plot_kline_chart/价值指数/创业板V.html">创业板V</a></li>
                        <li><a href="plot_kline_chart/价值指数/300 价值.html">300 价值</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">规模指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/规模指数/上证380.html">上证380</a></li>
                        <li><a href="plot_kline_chart/规模指数/上证180.html">上证180</a></li>
                        <li><a href="plot_kline_chart/规模指数/上证50.html">上证50</a></li>
                        <li><a href="plot_kline_chart/规模指数/超大盘.html">超大盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/上证中盘.html">上证中盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/上证小盘.html">上证小盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/上证中小.html">上证中小</a></li>
                        <li><a href="plot_kline_chart/规模指数/上证全指.html">上证全指</a></li>
                        <li><a href="plot_kline_chart/规模指数/市值百强.html">市值百强</a></li>
                        <li><a href="plot_kline_chart/规模指数/沪深300.html">沪深300</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证1000.html">中证1000</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证100.html">中证100</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证200.html">中证200</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证500.html">中证500</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证800.html">中证800</a></li>
                        <li><a href="plot_kline_chart/规模指数/两岸三地.html">两岸三地</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证成指.html">深证成指</a></li>
                        <li><a href="plot_kline_chart/规模指数/深成指R.html">深成指R</a></li>
                        <li><a href="plot_kline_chart/规模指数/成份Ｂ指.html">成份Ｂ指</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证100R.html">深证100R</a></li>
                        <li><a href="plot_kline_chart/规模指数/中小板指.html">中小板指</a></li>
                        <li><a href="plot_kline_chart/规模指数/创业板指.html">创业板指</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证300.html">深证300</a></li>
                        <li><a href="plot_kline_chart/规模指数/中小300.html">中小300</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证200.html">深证200</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证700.html">深证700</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证1000.html">深证1000</a></li>
                        <li><a href="plot_kline_chart/规模指数/创业300.html">创业300</a></li>
                        <li><a href="plot_kline_chart/规模指数/中小创新.html">中小创新</a></li>
                        <li><a href="plot_kline_chart/规模指数/沪深300.html">沪深300</a></li>
                        <li><a href="plot_kline_chart/规模指数/国证2000.html">国证2000</a></li>
                        <li><a href="plot_kline_chart/规模指数/国证50.html">国证50</a></li>
                        <li><a href="plot_kline_chart/规模指数/国证1000.html">国证1000</a></li>
                        <li><a href="plot_kline_chart/规模指数/国证300.html">国证300</a></li>
                        <li><a href="plot_kline_chart/规模指数/综企指巨潮100.html">综企指巨潮100</a></li>
                        <li><a href="plot_kline_chart/规模指数/巨潮大盘.html">巨潮大盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/巨潮中盘.html">巨潮中盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/巨潮小盘.html">巨潮小盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证100.html">深证100</a></li>
                        <li><a href="plot_kline_chart/规模指数/中小板R.html">中小板R</a></li>
                        <li><a href="plot_kline_chart/规模指数/深证300R.html">深证300R</a></li>
                        <li><a href="plot_kline_chart/规模指数/大中盘.html">大中盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/中小盘.html">中小盘</a></li>
                        <li><a href="plot_kline_chart/规模指数/创业板R.html">创业板R</a></li>
                        <li><a href="plot_kline_chart/规模指数/中创100R.html">中创100R</a></li>
                        <li><a href="plot_kline_chart/规模指数/中创100.html">中创100</a></li>
                        <li><a href="plot_kline_chart/规模指数/中小基础.html">中小基础</a></li>
                        <li><a href="plot_kline_chart/规模指数/中创400.html">中创400</a></li>
                        <li><a href="plot_kline_chart/规模指数/中创500.html">中创500</a></li>
                        <li><a href="plot_kline_chart/规模指数/创业基础.html">创业基础</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证100.html">中证100</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证 200.html">中证 200</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证 500.html">中证 500</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证 700.html">中证 700</a></li>
                        <li><a href="plot_kline_chart/规模指数/中证超大.html">中证超大</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">成长指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/成长指数/180成长.html">180成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/180R成长.html">180R成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/全指成长.html">全指成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/全R成长.html">全R成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/380成长.html">380成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/380R成长.html">380R成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/300成长.html">300成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/深证成长.html">深证成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/国证成长.html">国证成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/大盘成长.html">大盘成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/中盘成长.html">中盘成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/小盘成长.html">小盘成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/中小成长.html">中小成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/中创成长.html">中创成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/700成长.html">700成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/1000成长.html">1000成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/创业板G.html">创业板G</a></li>
                        <li><a href="plot_kline_chart/成长指数/300 成长.html">300 成长</a></li>
                        <li><a href="plot_kline_chart/成长指数/300R成长.html">300R成长</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">策略指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/策略指数/50等权.html">50等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/180等权.html">180等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/50基本.html">50基本</a></li>
                        <li><a href="plot_kline_chart/策略指数/180基本.html">180基本</a></li>
                        <li><a href="plot_kline_chart/策略指数/能源等权.html">能源等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/材料等权.html">材料等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/工业等权.html">工业等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/可选等权.html">可选等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/消费等权.html">消费等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/医药等权.html">医药等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/金融等权.html">金融等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/信息等权.html">信息等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/电信等权.html">电信等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/公用等权.html">公用等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/180分层.html">180分层</a></li>
                        <li><a href="plot_kline_chart/策略指数/上证F200.html">上证F200</a></li>
                        <li><a href="plot_kline_chart/策略指数/上证F300.html">上证F300</a></li>
                        <li><a href="plot_kline_chart/策略指数/上证F500.html">上证F500</a></li>
                        <li><a href="plot_kline_chart/策略指数/380等权.html">380等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/380基本.html">380基本</a></li>
                        <li><a href="plot_kline_chart/策略指数/180波动.html">180波动</a></li>
                        <li><a href="plot_kline_chart/策略指数/380波动.html">380波动</a></li>
                        <li><a href="plot_kline_chart/策略指数/180高贝.html">180高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/180低贝.html">180低贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/380高贝.html">380高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/380低贝.html">380低贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/300高贝.html">300高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/800等权.html">800等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/基本面50.html">基本面50</a></li>
                        <li><a href="plot_kline_chart/策略指数/基本400.html">基本400</a></li>
                        <li><a href="plot_kline_chart/策略指数/等权90.html">等权90</a></li>
                        <li><a href="plot_kline_chart/策略指数/500等权.html">500等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/300等权.html">300等权</a></li>
                        <li><a href="plot_kline_chart/策略指数/百发100.html">百发100</a></li>
                        <li><a href="plot_kline_chart/策略指数/大盘低波.html">大盘低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/大盘高贝.html">大盘高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/中盘低波.html">中盘低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/中盘高贝.html">中盘高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/小盘低波.html">小盘低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/小盘高贝.html">小盘高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/红利100.html">红利100</a></li>
                        <li><a href="plot_kline_chart/策略指数/专利领先.html">专利领先</a></li>
                        <li><a href="plot_kline_chart/策略指数/深100EW.html">深100EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/深300EW.html">深300EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/中小板EW.html">中小板EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/创业板EW.html">创业板EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/100低波.html">100低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/深证绩效.html">深证绩效</a></li>
                        <li><a href="plot_kline_chart/策略指数/100绩效.html">100绩效</a></li>
                        <li><a href="plot_kline_chart/策略指数/300绩效.html">300绩效</a></li>
                        <li><a href="plot_kline_chart/策略指数/中小绩效.html">中小绩效</a></li>
                        <li><a href="plot_kline_chart/策略指数/深成指EW.html">深成指EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/中创EW.html">中创EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/深证低波.html">深证低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/深证高贝.html">深证高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/中小低波.html">中小低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/中小高贝.html">中小高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/中创低波.html">中创低波</a></li>
                        <li><a href="plot_kline_chart/策略指数/中创高贝.html">中创高贝</a></li>
                        <li><a href="plot_kline_chart/策略指数/深红利50.html">深红利50</a></li>
                        <li><a href="plot_kline_chart/策略指数/创业板50.html">创业板50</a></li>
                        <li><a href="plot_kline_chart/策略指数/深医药EW.html">深医药EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/深互联EW.html">深互联EW</a></li>
                        <li><a href="plot_kline_chart/策略指数/深证F60.html">深证F60</a></li>
                        <li><a href="plot_kline_chart/策略指数/深证F120.html">深证F120</a></li>
                        <li><a href="plot_kline_chart/策略指数/深证F200.html">深证F200</a></li>
                        <li><a href="plot_kline_chart/策略指数/基本面50.html">基本面50</a></li>
                        <li><a href="plot_kline_chart/策略指数/500等权.html">500等权</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">主题指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/主题指数/红利指数.html">红利指数</a></li>
                        <li><a href="plot_kline_chart/主题指数/180金融.html">180金融</a></li>
                        <li><a href="plot_kline_chart/主题指数/治理指数.html">治理指数</a></li>
                        <li><a href="plot_kline_chart/主题指数/180治理.html">180治理</a></li>
                        <li><a href="plot_kline_chart/主题指数/180基建.html">180基建</a></li>
                        <li><a href="plot_kline_chart/主题指数/180资源.html">180资源</a></li>
                        <li><a href="plot_kline_chart/主题指数/180运输.html">180运输</a></li>
                        <li><a href="plot_kline_chart/主题指数/180R价值.html">180R价值</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证央企.html">上证央企</a></li>
                        <li><a href="plot_kline_chart/主题指数/责任指数.html">责任指数</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证民企.html">上证民企</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证地企.html">上证地企</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证国企.html">上证国企</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证沪企.html">上证沪企</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证周期.html">上证周期</a></li>
                        <li><a href="plot_kline_chart/主题指数/非周期.html">非周期</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证龙头.html">上证龙头</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证商品.html">上证商品</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证新兴.html">上证新兴</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证资源.html">上证资源</a></li>
                        <li><a href="plot_kline_chart/主题指数/消费80.html">消费80</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪财中小.html">沪财中小</a></li>
                        <li><a href="plot_kline_chart/主题指数/资源50.html">资源50</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证上游.html">上证上游</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证中游.html">上证中游</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证下游.html">上证下游</a></li>
                        <li><a href="plot_kline_chart/主题指数/高端装备.html">高端装备</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪投资品.html">沪投资品</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪消费品.html">沪消费品</a></li>
                        <li><a href="plot_kline_chart/主题指数/持续产业.html">持续产业</a></li>
                        <li><a href="plot_kline_chart/主题指数/医药主题.html">医药主题</a></li>
                        <li><a href="plot_kline_chart/主题指数/农业主题.html">农业主题</a></li>
                        <li><a href="plot_kline_chart/主题指数/180动态.html">180动态</a></li>
                        <li><a href="plot_kline_chart/主题指数/180稳定.html">180稳定</a></li>
                        <li><a href="plot_kline_chart/主题指数/消费50.html">消费50</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证高新.html">上证高新</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证100.html">上证100</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证150.html">上证150</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证银行.html">上证银行</a></li>
                        <li><a href="plot_kline_chart/主题指数/380动态.html">380动态</a></li>
                        <li><a href="plot_kline_chart/主题指数/380稳定.html">380稳定</a></li>
                        <li><a href="plot_kline_chart/主题指数/优势资源.html">优势资源</a></li>
                        <li><a href="plot_kline_chart/主题指数/优势制造.html">优势制造</a></li>
                        <li><a href="plot_kline_chart/主题指数/优势消费.html">优势消费</a></li>
                        <li><a href="plot_kline_chart/主题指数/消费领先.html">消费领先</a></li>
                        <li><a href="plot_kline_chart/主题指数/180红利.html">180红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/380红利.html">380红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/上国红利.html">上国红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/上央红利.html">上央红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/上民红利.html">上民红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/上证环保.html">上证环保</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪股通.html">沪股通</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪新丝路.html">沪新丝路</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪中国造.html">沪中国造</a></li>
                        <li><a href="plot_kline_chart/主题指数/沪互联+.html">沪互联+</a></li>
                        <li><a href="plot_kline_chart/主题指数/500沪市.html">500沪市</a></li>
                        <li><a href="plot_kline_chart/主题指数/A股资源.html">A股资源</a></li>
                        <li><a href="plot_kline_chart/主题指数/消费服务.html">消费服务</a></li>
                        <li><a href="plot_kline_chart/主题指数/食品饮料.html">食品饮料</a></li>
                        <li><a href="plot_kline_chart/主题指数/医药生物.html">医药生物</a></li>
                        <li><a href="plot_kline_chart/主题指数/细分医药.html">细分医药</a></li>
                        <li><a href="plot_kline_chart/主题指数/细分地产.html">细分地产</a></li>
                        <li><a href="plot_kline_chart/主题指数/兴证海峡.html">兴证海峡</a></li>
                        <li><a href="plot_kline_chart/主题指数/有色金属.html">有色金属</a></li>
                        <li><a href="plot_kline_chart/主题指数/300红利.html">300红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/800有色.html">800有色</a></li>
                        <li><a href="plot_kline_chart/主题指数/中证环保.html">中证环保</a></li>
                        <li><a href="plot_kline_chart/主题指数/ESG 100.html">ESG 100</a></li>
                        <li><a href="plot_kline_chart/主题指数/300非银.html">300非银</a></li>
                        <li><a href="plot_kline_chart/主题指数/300有色.html">300有色</a></li>
                        <li><a href="plot_kline_chart/主题指数/央视500.html">央视500</a></li>
                        <li><a href="plot_kline_chart/主题指数/小康指数.html">小康指数</a></li>
                        <li><a href="plot_kline_chart/主题指数/中证红利.html">中证红利</a></li>
                        <li><a href="plot_kline_chart/主题指数/民企200.html">民企200</a></li>
                        <li><a href="plot_kline_chart/主题指数/财富大盘.html">财富大盘</a></li>
                        <li><a href="plot_kline_chart/主题指数/内地资源.html">内地资源</a></li>
                        <li><a href="plot_kline_chart/主题指数/300基建.html">300基建</a></li>
                        <li><a href="plot_kline_chart/主题指数/创业成长.html">创业成长</a></li>
                        <li><a href="plot_kline_chart/主题指数/银河99.html">银河99</a></li>
                        <li><a href="plot_kline_chart/主题指数/中证上游.html">中证上游</a></li>
                        <li><a href="plot_kline_chart/主题指数/中证下游.html">中证下游</a></li>
                        <li><a href="plot_kline_chart/主题指数/中证新兴.html">中证新兴</a></li>
                        <li><a href="plot_kline_chart/主题指数/300非周.html">300非周</a></li>
                        <li><a href="plot_kline_chart/主题指数/技术领先.html">技术领先</a></li>
                        <li><a href="plot_kline_chart/主题指数/800金融.html">800金融</a></li>
                        <li><a href="plot_kline_chart/主题指数/钱江30.html">钱江30</a></li>
                        <li><a href="plot_kline_chart/主题指数/新华金牛.html">新华金牛</a></li>
                        <li><a href="plot_kline_chart/主题指数/内地低碳.html">内地低碳</a></li>
                        <li><a href="plot_kline_chart/主题指数/医药100.html">医药100</a></li>
                        <li><a href="plot_kline_chart/主题指数/大宗商品.html">大宗商品</a></li>
                        <li><a href="plot_kline_chart/主题指数/智能资产.html">智能资产</a></li>
                        <li><a href="plot_kline_chart/主题指数/领先行业.html">领先行业</a></li>
                        <li><a href="plot_kline_chart/主题指数/大消费.html">大消费</a></li>
                        <li><a href="plot_kline_chart/主题指数/中证TMT.html">中证TMT</a></li>
                        <li><a href="plot_kline_chart/主题指数/深市精选.html">深市精选</a></li>
                        <li><a href="plot_kline_chart/主题指数/资源优势.html">资源优势</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">一级行业指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/一级行业指数/上证能源.html">上证能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证材料.html">上证材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证工业.html">上证工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证可选.html">上证可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证消费.html">上证消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证医药.html">上证医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证金融.html">上证金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证信息.html">上证信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证电信.html">上证电信</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/上证公用.html">上证公用</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380能源.html">380能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380材料.html">380材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380工业.html">380工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380可选.html">380可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380消费.html">380消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380医药.html">380医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380金融.html">380金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380信息.html">380信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380电信.html">380电信</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/380公用.html">380公用</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300能源.html">300能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300材料.html">300材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300工业.html">300工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300可选.html">300可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300消费.html">300消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300医药.html">300医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300金融.html">300金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300公用.html">300公用</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证能源.html">中证能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证可选.html">中证可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证消费.html">中证消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证金融.html">中证金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证信息.html">中证信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指能源.html">全指能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指材料.html">全指材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指可选.html">全指可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指消费.html">全指消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指医药.html">全指医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指金融.html">全指金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/全指信息.html">全指信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000能源.html">1000能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000材料.html">1000材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000工业.html">1000工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000可选.html">1000可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000消费.html">1000消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000医药.html">1000医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000金融.html">1000金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000信息.html">1000信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证通信.html">国证通信</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/1000公用.html">1000公用</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证银行.html">国证银行</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证汽车.html">国证汽车</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证交运.html">国证交运</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证传媒.html">国证传媒</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证农牧.html">国证农牧</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证煤炭.html">国证煤炭</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证证券.html">国证证券</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证电力.html">国证电力</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证油气.html">国证油气</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/国证钢铁.html">国证钢铁</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证能源.html">深证能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证材料.html">深证材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证工业.html">深证工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证可选.html">深证可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证消费.html">深证消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证医药.html">深证医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证金融.html">深证金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证信息.html">深证信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证电信.html">深证电信</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深证公用.html">深证公用</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深A医药.html">深A医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/深互联网.html">深互联网</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 能源.html">300 能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 材料.html">300 材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 工业.html">300 工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 可选.html">300 可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 消费.html">300 消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 医药.html">300 医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 金融.html">300 金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 信息.html">300 信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 电信.html">300 电信</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/300 公用.html">300 公用</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证能源.html">中证能源</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证材料.html">中证材料</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证工业.html">中证工业</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证可选.html">中证可选</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证消费.html">中证消费</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证金融.html">中证金融</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证信息.html">中证信息</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证电信.html">中证电信</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="plot_kline_chart/一级行业指数/基建工程.html">基建工程</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">二级行业指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="plot_kline_chart/二级行业指数/800医药.html">800医药</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/500原料.html">500原料</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/500工业.html">500工业</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/500医药.html">500医药</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/500信息.html">500信息</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/300银行.html">300银行</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/300地产.html">300地产</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/300运输.html">300运输</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/300银行.html">300银行</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/300地产.html">300地产</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/300运输.html">300运输</a></li>
                        <li><a href="plot_kline_chart/二级行业指数/800地产.html">800地产</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    </div>
</header>
</body>
</html>
'''

HTML_SAMPLE = '''
        <!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <!-- custom CSS -->
    <link href="../../../core/resources/css/main.css" rel="stylesheet" type="text/css"/>
    <script type="text/javascript" src="../../../core/resources/assets/echarts.min.js"></script>
    <title>Home</title>
</head>
<body>
<!-- Header -->
<header id="header" class="header">
    <div class="header_down container wrapper clearfix bigmegamenu">
        <!--Main Menu HTML Code-->
        <nav class="wsmenu slideLeft clearfix">
            <ul class="mobile-sub wsmenu-list">
                <li class="active">
                    <span class="wsmenu-click"></span>
                    <a href="">综合指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../综合指数/上证指数.html">上证指数</a></li>
                        <li><a href="../综合指数/Ａ股指数.html">Ａ股指数</a></li>
                        <li><a href="../综合指数/B股指数.html">B股指数</a></li>
                        <li><a href="../综合指数/工业指数.html">工业指数</a></li>
                        <li><a href="../综合指数/商业指数.html">商业指数</a></li>
                        <li><a href="../综合指数/地产指数.html">地产指数</a></li>
                        <li><a href="../综合指数/公用指数.html">公用指数</a></li>
                        <li><a href="../综合指数/综合指数.html">综合指数</a></li>
                        <li><a href="../综合指数/新综指.html">新综指</a></li>
                        <li><a href="../综合指数/中型综指.html">中型综指</a></li>
                        <li><a href="../综合指数/上证流通.html">上证流通</a></li>
                        <li><a href="../综合指数/新 指 数.html">新 指 数</a></li>
                        <li><a href="../综合指数/中小板综.html">中小板综</a></li>
                        <li><a href="../综合指数/创业板综.html">创业板综</a></li>
                        <li><a href="../综合指数/深证综指.html">深证综指</a></li>
                        <li><a href="../综合指数/深证A指.html">深证A指</a></li>
                        <li><a href="../综合指数/深证B指.html">深证B指</a></li>
                        <li><a href="../综合指数/农林指数.html">农林指数</a></li>
                        <li><a href="../综合指数/采矿指数.html">采矿指数</a></li>
                        <li><a href="../综合指数/制造指数.html">制造指数</a></li>
                        <li><a href="../综合指数/水电指数.html">水电指数</a></li>
                        <li><a href="../综合指数/建筑指数.html">建筑指数</a></li>
                        <li><a href="../综合指数/批零指数.html">批零指数</a></li>
                        <li><a href="../综合指数/运输指数.html">运输指数</a></li>
                        <li><a href="../综合指数/住宿餐饮指数.html">住宿餐饮指数</a></li>
                        <li><a href="../综合指数/IT指数.html">IT指数</a></li>
                        <li><a href="../综合指数/金融指数.html">金融指数</a></li>
                        <li><a href="../综合指数/地产指数.html">地产指数</a></li>
                        <li><a href="../综合指数/商务指数.html">商务指数</a></li>
                        <li><a href="../综合指数/科研指数.html">科研指数</a></li>
                        <li><a href="../综合指数/公共指数.html">公共指数</a></li>
                        <li><a href="../综合指数/文化指数.html">文化指数</a></li>
                        <li><a href="../综合指数/综企指数.html">综企指数</a></li>
                        <li><a href="../综合指数/国证Ａ指.html">国证Ａ指</a></li>
                        <li><a href="../综合指数/国证Ｂ指.html">国证Ｂ指</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">基金指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../基金指数/基金指数.html">基金指数</a></li>
                        <li><a href="../基金指数/乐富指数.html">乐富指数</a></li>
                        <li><a href="../基金指数/基金指数.html">基金指数</a></li>
                        <li><a href="../基金指数/深证ETF.html">深证ETF</a></li>
                        <li><a href="../基金指数/国证基金.html">国证基金</a></li>
                        <li><a href="../基金指数/国证ETF.html">国证ETF</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">债券指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../债券指数/国债指数.html">国债指数</a></li>
                        <li><a href="../债券指数/企债指数.html">企债指数</a></li>
                        <li><a href="../债券指数/沪公司债.html">沪公司债</a></li>
                        <li><a href="../债券指数/沪企债30.html">沪企债30</a></li>
                        <li><a href="../债券指数/5年信用.html">5年信用</a></li>
                        <li><a href="../债券指数/信用100.html">信用100</a></li>
                        <li><a href="../债券指数/上证转债.html">上证转债</a></li>
                        <li><a href="../债券指数/中证转债.html">中证转债</a></li>
                        <li><a href="../债券指数/中高企债.html">中高企债</a></li>
                        <li><a href="../债券指数/深信中高.html">深信中高</a></li>
                        <li><a href="../债券指数/深信中低.html">深信中低</a></li>
                        <li><a href="../债券指数/深信用债.html">深信用债</a></li>
                        <li><a href="../债券指数/深公司债.html">深公司债</a></li>
                        <li><a href="../债券指数/深证转债.html">深证转债</a></li>
                        <li><a href="../债券指数/深证转债.html">深证转债</a></li>
                        <li><a href="../债券指数/企债指数.html">企债指数</a></li>
                        <li><a href="../债券指数/公司债指.html">公司债指</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">价值指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../价值指数/180价值.html">180价值</a></li>
                        <li><a href="../价值指数/180R价值.html">180R价值</a></li>
                        <li><a href="../价值指数/全指价值.html">全指价值</a></li>
                        <li><a href="../价值指数/全R价值.html">全R价值</a></li>
                        <li><a href="../价值指数/380价值.html">380价值</a></li>
                        <li><a href="../价值指数/380R价值.html">380R价值</a></li>
                        <li><a href="../价值指数/300价值.html">300价值</a></li>
                        <li><a href="../价值指数/深证价值.html">深证价值</a></li>
                        <li><a href="../价值指数/国证价值.html">国证价值</a></li>
                        <li><a href="../价值指数/大盘价值.html">大盘价值</a></li>
                        <li><a href="../价值指数/中盘价值.html">中盘价值</a></li>
                        <li><a href="../价值指数/小盘价值.html">小盘价值</a></li>
                        <li><a href="../价值指数/中小价值.html">中小价值</a></li>
                        <li><a href="../价值指数/中创价值.html">中创价值</a></li>
                        <li><a href="../价值指数/700价值.html">700价值</a></li>
                        <li><a href="../价值指数/1000价值.html">1000价值</a></li>
                        <li><a href="../价值指数/创业板V.html">创业板V</a></li>
                        <li><a href="../价值指数/300 价值.html">300 价值</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">规模指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../规模指数/上证380.html">上证380</a></li>
                        <li><a href="../规模指数/上证180.html">上证180</a></li>
                        <li><a href="../规模指数/上证50.html">上证50</a></li>
                        <li><a href="../规模指数/超大盘.html">超大盘</a></li>
                        <li><a href="../规模指数/上证中盘.html">上证中盘</a></li>
                        <li><a href="../规模指数/上证小盘.html">上证小盘</a></li>
                        <li><a href="../规模指数/上证中小.html">上证中小</a></li>
                        <li><a href="../规模指数/上证全指.html">上证全指</a></li>
                        <li><a href="../规模指数/市值百强.html">市值百强</a></li>
                        <li><a href="../规模指数/沪深300.html">沪深300</a></li>
                        <li><a href="../规模指数/中证1000.html">中证1000</a></li>
                        <li><a href="../规模指数/中证100.html">中证100</a></li>
                        <li><a href="../规模指数/中证200.html">中证200</a></li>
                        <li><a href="../规模指数/中证500.html">中证500</a></li>
                        <li><a href="../规模指数/中证800.html">中证800</a></li>
                        <li><a href="../规模指数/两岸三地.html">两岸三地</a></li>
                        <li><a href="../规模指数/深证成指.html">深证成指</a></li>
                        <li><a href="../规模指数/深成指R.html">深成指R</a></li>
                        <li><a href="../规模指数/成份Ｂ指.html">成份Ｂ指</a></li>
                        <li><a href="../规模指数/深证100R.html">深证100R</a></li>
                        <li><a href="../规模指数/中小板指.html">中小板指</a></li>
                        <li><a href="../规模指数/创业板指.html">创业板指</a></li>
                        <li><a href="../规模指数/深证300.html">深证300</a></li>
                        <li><a href="../规模指数/中小300.html">中小300</a></li>
                        <li><a href="../规模指数/深证200.html">深证200</a></li>
                        <li><a href="../规模指数/深证700.html">深证700</a></li>
                        <li><a href="../规模指数/深证1000.html">深证1000</a></li>
                        <li><a href="../规模指数/创业300.html">创业300</a></li>
                        <li><a href="../规模指数/中小创新.html">中小创新</a></li>
                        <li><a href="../规模指数/沪深300.html">沪深300</a></li>
                        <li><a href="../规模指数/国证2000.html">国证2000</a></li>
                        <li><a href="../规模指数/国证50.html">国证50</a></li>
                        <li><a href="../规模指数/国证1000.html">国证1000</a></li>
                        <li><a href="../规模指数/国证300.html">国证300</a></li>
                        <li><a href="../规模指数/综企指巨潮100.html">综企指巨潮100</a></li>
                        <li><a href="../规模指数/巨潮大盘.html">巨潮大盘</a></li>
                        <li><a href="../规模指数/巨潮中盘.html">巨潮中盘</a></li>
                        <li><a href="../规模指数/巨潮小盘.html">巨潮小盘</a></li>
                        <li><a href="../规模指数/深证100.html">深证100</a></li>
                        <li><a href="../规模指数/中小板R.html">中小板R</a></li>
                        <li><a href="../规模指数/深证300R.html">深证300R</a></li>
                        <li><a href="../规模指数/大中盘.html">大中盘</a></li>
                        <li><a href="../规模指数/中小盘.html">中小盘</a></li>
                        <li><a href="../规模指数/创业板R.html">创业板R</a></li>
                        <li><a href="../规模指数/中创100R.html">中创100R</a></li>
                        <li><a href="../规模指数/中创100.html">中创100</a></li>
                        <li><a href="../规模指数/中小基础.html">中小基础</a></li>
                        <li><a href="../规模指数/中创400.html">中创400</a></li>
                        <li><a href="../规模指数/中创500.html">中创500</a></li>
                        <li><a href="../规模指数/创业基础.html">创业基础</a></li>
                        <li><a href="../规模指数/中证100.html">中证100</a></li>
                        <li><a href="../规模指数/中证 200.html">中证 200</a></li>
                        <li><a href="../规模指数/中证 500.html">中证 500</a></li>
                        <li><a href="../规模指数/中证 700.html">中证 700</a></li>
                        <li><a href="../规模指数/中证超大.html">中证超大</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">成长指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../成长指数/180成长.html">180成长</a></li>
                        <li><a href="../成长指数/180R成长.html">180R成长</a></li>
                        <li><a href="../成长指数/全指成长.html">全指成长</a></li>
                        <li><a href="../成长指数/全R成长.html">全R成长</a></li>
                        <li><a href="../成长指数/380成长.html">380成长</a></li>
                        <li><a href="../成长指数/380R成长.html">380R成长</a></li>
                        <li><a href="../成长指数/300成长.html">300成长</a></li>
                        <li><a href="../成长指数/深证成长.html">深证成长</a></li>
                        <li><a href="../成长指数/国证成长.html">国证成长</a></li>
                        <li><a href="../成长指数/大盘成长.html">大盘成长</a></li>
                        <li><a href="../成长指数/中盘成长.html">中盘成长</a></li>
                        <li><a href="../成长指数/小盘成长.html">小盘成长</a></li>
                        <li><a href="../成长指数/中小成长.html">中小成长</a></li>
                        <li><a href="../成长指数/中创成长.html">中创成长</a></li>
                        <li><a href="../成长指数/700成长.html">700成长</a></li>
                        <li><a href="../成长指数/1000成长.html">1000成长</a></li>
                        <li><a href="../成长指数/创业板G.html">创业板G</a></li>
                        <li><a href="../成长指数/300 成长.html">300 成长</a></li>
                        <li><a href="../成长指数/300R成长.html">300R成长</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">策略指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../策略指数/50等权.html">50等权</a></li>
                        <li><a href="../策略指数/180等权.html">180等权</a></li>
                        <li><a href="../策略指数/50基本.html">50基本</a></li>
                        <li><a href="../策略指数/180基本.html">180基本</a></li>
                        <li><a href="../策略指数/能源等权.html">能源等权</a></li>
                        <li><a href="../策略指数/材料等权.html">材料等权</a></li>
                        <li><a href="../策略指数/工业等权.html">工业等权</a></li>
                        <li><a href="../策略指数/可选等权.html">可选等权</a></li>
                        <li><a href="../策略指数/消费等权.html">消费等权</a></li>
                        <li><a href="../策略指数/医药等权.html">医药等权</a></li>
                        <li><a href="../策略指数/金融等权.html">金融等权</a></li>
                        <li><a href="../策略指数/信息等权.html">信息等权</a></li>
                        <li><a href="../策略指数/电信等权.html">电信等权</a></li>
                        <li><a href="../策略指数/公用等权.html">公用等权</a></li>
                        <li><a href="../策略指数/180分层.html">180分层</a></li>
                        <li><a href="../策略指数/上证F200.html">上证F200</a></li>
                        <li><a href="../策略指数/上证F300.html">上证F300</a></li>
                        <li><a href="../策略指数/上证F500.html">上证F500</a></li>
                        <li><a href="../策略指数/380等权.html">380等权</a></li>
                        <li><a href="../策略指数/380基本.html">380基本</a></li>
                        <li><a href="../策略指数/180波动.html">180波动</a></li>
                        <li><a href="../策略指数/380波动.html">380波动</a></li>
                        <li><a href="../策略指数/180高贝.html">180高贝</a></li>
                        <li><a href="../策略指数/180低贝.html">180低贝</a></li>
                        <li><a href="../策略指数/380高贝.html">380高贝</a></li>
                        <li><a href="../策略指数/380低贝.html">380低贝</a></li>
                        <li><a href="../策略指数/300高贝.html">300高贝</a></li>
                        <li><a href="../策略指数/800等权.html">800等权</a></li>
                        <li><a href="../策略指数/基本面50.html">基本面50</a></li>
                        <li><a href="../策略指数/基本400.html">基本400</a></li>
                        <li><a href="../策略指数/等权90.html">等权90</a></li>
                        <li><a href="../策略指数/500等权.html">500等权</a></li>
                        <li><a href="../策略指数/300等权.html">300等权</a></li>
                        <li><a href="../策略指数/百发100.html">百发100</a></li>
                        <li><a href="../策略指数/大盘低波.html">大盘低波</a></li>
                        <li><a href="../策略指数/大盘高贝.html">大盘高贝</a></li>
                        <li><a href="../策略指数/中盘低波.html">中盘低波</a></li>
                        <li><a href="../策略指数/中盘高贝.html">中盘高贝</a></li>
                        <li><a href="../策略指数/小盘低波.html">小盘低波</a></li>
                        <li><a href="../策略指数/小盘高贝.html">小盘高贝</a></li>
                        <li><a href="../策略指数/红利100.html">红利100</a></li>
                        <li><a href="../策略指数/专利领先.html">专利领先</a></li>
                        <li><a href="../策略指数/深100EW.html">深100EW</a></li>
                        <li><a href="../策略指数/深300EW.html">深300EW</a></li>
                        <li><a href="../策略指数/中小板EW.html">中小板EW</a></li>
                        <li><a href="../策略指数/创业板EW.html">创业板EW</a></li>
                        <li><a href="../策略指数/100低波.html">100低波</a></li>
                        <li><a href="../策略指数/深证绩效.html">深证绩效</a></li>
                        <li><a href="../策略指数/100绩效.html">100绩效</a></li>
                        <li><a href="../策略指数/300绩效.html">300绩效</a></li>
                        <li><a href="../策略指数/中小绩效.html">中小绩效</a></li>
                        <li><a href="../策略指数/深成指EW.html">深成指EW</a></li>
                        <li><a href="../策略指数/中创EW.html">中创EW</a></li>
                        <li><a href="../策略指数/深证低波.html">深证低波</a></li>
                        <li><a href="../策略指数/深证高贝.html">深证高贝</a></li>
                        <li><a href="../策略指数/中小低波.html">中小低波</a></li>
                        <li><a href="../策略指数/中小高贝.html">中小高贝</a></li>
                        <li><a href="../策略指数/中创低波.html">中创低波</a></li>
                        <li><a href="../策略指数/中创高贝.html">中创高贝</a></li>
                        <li><a href="../策略指数/深红利50.html">深红利50</a></li>
                        <li><a href="../策略指数/创业板50.html">创业板50</a></li>
                        <li><a href="../策略指数/深医药EW.html">深医药EW</a></li>
                        <li><a href="../策略指数/深互联EW.html">深互联EW</a></li>
                        <li><a href="../策略指数/深证F60.html">深证F60</a></li>
                        <li><a href="../策略指数/深证F120.html">深证F120</a></li>
                        <li><a href="../策略指数/深证F200.html">深证F200</a></li>
                        <li><a href="../策略指数/基本面50.html">基本面50</a></li>
                        <li><a href="../策略指数/500等权.html">500等权</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">主题指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../主题指数/红利指数.html">红利指数</a></li>
                        <li><a href="../主题指数/180金融.html">180金融</a></li>
                        <li><a href="../主题指数/治理指数.html">治理指数</a></li>
                        <li><a href="../主题指数/180治理.html">180治理</a></li>
                        <li><a href="../主题指数/180基建.html">180基建</a></li>
                        <li><a href="../主题指数/180资源.html">180资源</a></li>
                        <li><a href="../主题指数/180运输.html">180运输</a></li>
                        <li><a href="../主题指数/180R价值.html">180R价值</a></li>
                        <li><a href="../主题指数/上证央企.html">上证央企</a></li>
                        <li><a href="../主题指数/责任指数.html">责任指数</a></li>
                        <li><a href="../主题指数/上证民企.html">上证民企</a></li>
                        <li><a href="../主题指数/上证地企.html">上证地企</a></li>
                        <li><a href="../主题指数/上证国企.html">上证国企</a></li>
                        <li><a href="../主题指数/上证沪企.html">上证沪企</a></li>
                        <li><a href="../主题指数/上证周期.html">上证周期</a></li>
                        <li><a href="../主题指数/非周期.html">非周期</a></li>
                        <li><a href="../主题指数/上证龙头.html">上证龙头</a></li>
                        <li><a href="../主题指数/上证商品.html">上证商品</a></li>
                        <li><a href="../主题指数/上证新兴.html">上证新兴</a></li>
                        <li><a href="../主题指数/上证资源.html">上证资源</a></li>
                        <li><a href="../主题指数/消费80.html">消费80</a></li>
                        <li><a href="../主题指数/沪财中小.html">沪财中小</a></li>
                        <li><a href="../主题指数/资源50.html">资源50</a></li>
                        <li><a href="../主题指数/上证上游.html">上证上游</a></li>
                        <li><a href="../主题指数/上证中游.html">上证中游</a></li>
                        <li><a href="../主题指数/上证下游.html">上证下游</a></li>
                        <li><a href="../主题指数/高端装备.html">高端装备</a></li>
                        <li><a href="../主题指数/沪投资品.html">沪投资品</a></li>
                        <li><a href="../主题指数/沪消费品.html">沪消费品</a></li>
                        <li><a href="../主题指数/持续产业.html">持续产业</a></li>
                        <li><a href="../主题指数/医药主题.html">医药主题</a></li>
                        <li><a href="../主题指数/农业主题.html">农业主题</a></li>
                        <li><a href="../主题指数/180动态.html">180动态</a></li>
                        <li><a href="../主题指数/180稳定.html">180稳定</a></li>
                        <li><a href="../主题指数/消费50.html">消费50</a></li>
                        <li><a href="../主题指数/上证高新.html">上证高新</a></li>
                        <li><a href="../主题指数/上证100.html">上证100</a></li>
                        <li><a href="../主题指数/上证150.html">上证150</a></li>
                        <li><a href="../主题指数/上证银行.html">上证银行</a></li>
                        <li><a href="../主题指数/380动态.html">380动态</a></li>
                        <li><a href="../主题指数/380稳定.html">380稳定</a></li>
                        <li><a href="../主题指数/优势资源.html">优势资源</a></li>
                        <li><a href="../主题指数/优势制造.html">优势制造</a></li>
                        <li><a href="../主题指数/优势消费.html">优势消费</a></li>
                        <li><a href="../主题指数/消费领先.html">消费领先</a></li>
                        <li><a href="../主题指数/180红利.html">180红利</a></li>
                        <li><a href="../主题指数/380红利.html">380红利</a></li>
                        <li><a href="../主题指数/上国红利.html">上国红利</a></li>
                        <li><a href="../主题指数/上央红利.html">上央红利</a></li>
                        <li><a href="../主题指数/上民红利.html">上民红利</a></li>
                        <li><a href="../主题指数/上证环保.html">上证环保</a></li>
                        <li><a href="../主题指数/沪股通.html">沪股通</a></li>
                        <li><a href="../主题指数/沪新丝路.html">沪新丝路</a></li>
                        <li><a href="../主题指数/沪中国造.html">沪中国造</a></li>
                        <li><a href="../主题指数/沪互联+.html">沪互联+</a></li>
                        <li><a href="../主题指数/500沪市.html">500沪市</a></li>
                        <li><a href="../主题指数/A股资源.html">A股资源</a></li>
                        <li><a href="../主题指数/消费服务.html">消费服务</a></li>
                        <li><a href="../主题指数/食品饮料.html">食品饮料</a></li>
                        <li><a href="../主题指数/医药生物.html">医药生物</a></li>
                        <li><a href="../主题指数/细分医药.html">细分医药</a></li>
                        <li><a href="../主题指数/细分地产.html">细分地产</a></li>
                        <li><a href="../主题指数/兴证海峡.html">兴证海峡</a></li>
                        <li><a href="../主题指数/有色金属.html">有色金属</a></li>
                        <li><a href="../主题指数/300红利.html">300红利</a></li>
                        <li><a href="../主题指数/800有色.html">800有色</a></li>
                        <li><a href="../主题指数/中证环保.html">中证环保</a></li>
                        <li><a href="../主题指数/ESG 100.html">ESG 100</a></li>
                        <li><a href="../主题指数/300非银.html">300非银</a></li>
                        <li><a href="../主题指数/300有色.html">300有色</a></li>
                        <li><a href="../主题指数/央视500.html">央视500</a></li>
                        <li><a href="../主题指数/小康指数.html">小康指数</a></li>
                        <li><a href="../主题指数/中证红利.html">中证红利</a></li>
                        <li><a href="../主题指数/民企200.html">民企200</a></li>
                        <li><a href="../主题指数/财富大盘.html">财富大盘</a></li>
                        <li><a href="../主题指数/内地资源.html">内地资源</a></li>
                        <li><a href="../主题指数/300基建.html">300基建</a></li>
                        <li><a href="../主题指数/创业成长.html">创业成长</a></li>
                        <li><a href="../主题指数/银河99.html">银河99</a></li>
                        <li><a href="../主题指数/中证上游.html">中证上游</a></li>
                        <li><a href="../主题指数/中证下游.html">中证下游</a></li>
                        <li><a href="../主题指数/中证新兴.html">中证新兴</a></li>
                        <li><a href="../主题指数/300非周.html">300非周</a></li>
                        <li><a href="../主题指数/技术领先.html">技术领先</a></li>
                        <li><a href="../主题指数/800金融.html">800金融</a></li>
                        <li><a href="../主题指数/钱江30.html">钱江30</a></li>
                        <li><a href="../主题指数/新华金牛.html">新华金牛</a></li>
                        <li><a href="../主题指数/内地低碳.html">内地低碳</a></li>
                        <li><a href="../主题指数/医药100.html">医药100</a></li>
                        <li><a href="../主题指数/大宗商品.html">大宗商品</a></li>
                        <li><a href="../主题指数/智能资产.html">智能资产</a></li>
                        <li><a href="../主题指数/领先行业.html">领先行业</a></li>
                        <li><a href="../主题指数/大消费.html">大消费</a></li>
                        <li><a href="../主题指数/中证TMT.html">中证TMT</a></li>
                        <li><a href="../主题指数/深市精选.html">深市精选</a></li>
                        <li><a href="../主题指数/资源优势.html">资源优势</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">一级行业指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../一级行业指数/上证能源.html">上证能源</a></li>
                        <li><a href="../一级行业指数/上证材料.html">上证材料</a></li>
                        <li><a href="../一级行业指数/上证工业.html">上证工业</a></li>
                        <li><a href="../一级行业指数/上证可选.html">上证可选</a></li>
                        <li><a href="../一级行业指数/上证消费.html">上证消费</a></li>
                        <li><a href="../一级行业指数/上证医药.html">上证医药</a></li>
                        <li><a href="../一级行业指数/上证金融.html">上证金融</a></li>
                        <li><a href="../一级行业指数/上证信息.html">上证信息</a></li>
                        <li><a href="../一级行业指数/上证电信.html">上证电信</a></li>
                        <li><a href="../一级行业指数/上证公用.html">上证公用</a></li>
                        <li><a href="../一级行业指数/380能源.html">380能源</a></li>
                        <li><a href="../一级行业指数/380材料.html">380材料</a></li>
                        <li><a href="../一级行业指数/380工业.html">380工业</a></li>
                        <li><a href="../一级行业指数/380可选.html">380可选</a></li>
                        <li><a href="../一级行业指数/380消费.html">380消费</a></li>
                        <li><a href="../一级行业指数/380医药.html">380医药</a></li>
                        <li><a href="../一级行业指数/380金融.html">380金融</a></li>
                        <li><a href="../一级行业指数/380信息.html">380信息</a></li>
                        <li><a href="../一级行业指数/380电信.html">380电信</a></li>
                        <li><a href="../一级行业指数/380公用.html">380公用</a></li>
                        <li><a href="../一级行业指数/300能源.html">300能源</a></li>
                        <li><a href="../一级行业指数/300材料.html">300材料</a></li>
                        <li><a href="../一级行业指数/300工业.html">300工业</a></li>
                        <li><a href="../一级行业指数/300可选.html">300可选</a></li>
                        <li><a href="../一级行业指数/300消费.html">300消费</a></li>
                        <li><a href="../一级行业指数/300医药.html">300医药</a></li>
                        <li><a href="../一级行业指数/300金融.html">300金融</a></li>
                        <li><a href="../一级行业指数/300公用.html">300公用</a></li>
                        <li><a href="../一级行业指数/中证能源.html">中证能源</a></li>
                        <li><a href="../一级行业指数/中证可选.html">中证可选</a></li>
                        <li><a href="../一级行业指数/中证消费.html">中证消费</a></li>
                        <li><a href="../一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="../一级行业指数/中证金融.html">中证金融</a></li>
                        <li><a href="../一级行业指数/中证信息.html">中证信息</a></li>
                        <li><a href="../一级行业指数/全指能源.html">全指能源</a></li>
                        <li><a href="../一级行业指数/全指材料.html">全指材料</a></li>
                        <li><a href="../一级行业指数/全指可选.html">全指可选</a></li>
                        <li><a href="../一级行业指数/全指消费.html">全指消费</a></li>
                        <li><a href="../一级行业指数/全指医药.html">全指医药</a></li>
                        <li><a href="../一级行业指数/全指金融.html">全指金融</a></li>
                        <li><a href="../一级行业指数/全指信息.html">全指信息</a></li>
                        <li><a href="../一级行业指数/1000能源.html">1000能源</a></li>
                        <li><a href="../一级行业指数/1000材料.html">1000材料</a></li>
                        <li><a href="../一级行业指数/1000工业.html">1000工业</a></li>
                        <li><a href="../一级行业指数/1000可选.html">1000可选</a></li>
                        <li><a href="../一级行业指数/1000消费.html">1000消费</a></li>
                        <li><a href="../一级行业指数/1000医药.html">1000医药</a></li>
                        <li><a href="../一级行业指数/1000金融.html">1000金融</a></li>
                        <li><a href="../一级行业指数/1000信息.html">1000信息</a></li>
                        <li><a href="../一级行业指数/国证通信.html">国证通信</a></li>
                        <li><a href="../一级行业指数/1000公用.html">1000公用</a></li>
                        <li><a href="../一级行业指数/国证银行.html">国证银行</a></li>
                        <li><a href="../一级行业指数/国证汽车.html">国证汽车</a></li>
                        <li><a href="../一级行业指数/国证交运.html">国证交运</a></li>
                        <li><a href="../一级行业指数/国证传媒.html">国证传媒</a></li>
                        <li><a href="../一级行业指数/国证农牧.html">国证农牧</a></li>
                        <li><a href="../一级行业指数/国证煤炭.html">国证煤炭</a></li>
                        <li><a href="../一级行业指数/国证证券.html">国证证券</a></li>
                        <li><a href="../一级行业指数/国证电力.html">国证电力</a></li>
                        <li><a href="../一级行业指数/国证油气.html">国证油气</a></li>
                        <li><a href="../一级行业指数/国证钢铁.html">国证钢铁</a></li>
                        <li><a href="../一级行业指数/深证能源.html">深证能源</a></li>
                        <li><a href="../一级行业指数/深证材料.html">深证材料</a></li>
                        <li><a href="../一级行业指数/深证工业.html">深证工业</a></li>
                        <li><a href="../一级行业指数/深证可选.html">深证可选</a></li>
                        <li><a href="../一级行业指数/深证消费.html">深证消费</a></li>
                        <li><a href="../一级行业指数/深证医药.html">深证医药</a></li>
                        <li><a href="../一级行业指数/深证金融.html">深证金融</a></li>
                        <li><a href="../一级行业指数/深证信息.html">深证信息</a></li>
                        <li><a href="../一级行业指数/深证电信.html">深证电信</a></li>
                        <li><a href="../一级行业指数/深证公用.html">深证公用</a></li>
                        <li><a href="../一级行业指数/深A医药.html">深A医药</a></li>
                        <li><a href="../一级行业指数/深互联网.html">深互联网</a></li>
                        <li><a href="../一级行业指数/300 能源.html">300 能源</a></li>
                        <li><a href="../一级行业指数/300 材料.html">300 材料</a></li>
                        <li><a href="../一级行业指数/300 工业.html">300 工业</a></li>
                        <li><a href="../一级行业指数/300 可选.html">300 可选</a></li>
                        <li><a href="../一级行业指数/300 消费.html">300 消费</a></li>
                        <li><a href="../一级行业指数/300 医药.html">300 医药</a></li>
                        <li><a href="../一级行业指数/300 金融.html">300 金融</a></li>
                        <li><a href="../一级行业指数/300 信息.html">300 信息</a></li>
                        <li><a href="../一级行业指数/300 电信.html">300 电信</a></li>
                        <li><a href="../一级行业指数/300 公用.html">300 公用</a></li>
                        <li><a href="../一级行业指数/中证能源.html">中证能源</a></li>
                        <li><a href="../一级行业指数/中证材料.html">中证材料</a></li>
                        <li><a href="../一级行业指数/中证工业.html">中证工业</a></li>
                        <li><a href="../一级行业指数/中证可选.html">中证可选</a></li>
                        <li><a href="../一级行业指数/中证消费.html">中证消费</a></li>
                        <li><a href="../一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="../一级行业指数/中证金融.html">中证金融</a></li>
                        <li><a href="../一级行业指数/中证信息.html">中证信息</a></li>
                        <li><a href="../一级行业指数/中证电信.html">中证电信</a></li>
                        <li><a href="../一级行业指数/中证医药.html">中证医药</a></li>
                        <li><a href="../一级行业指数/基建工程.html">基建工程</a></li>
                    </ul>
                </li>
                <li>
                    <span class="wsmenu-click"></span>
                    <a href="">二级行业指数
                        <span class="arrow"></span>
                    </a>
                    <ul class="wsmenu-submenu">
                        <li><a href="../二级行业指数/800医药.html">800医药</a></li>
                        <li><a href="../二级行业指数/500原料.html">500原料</a></li>
                        <li><a href="../二级行业指数/500工业.html">500工业</a></li>
                        <li><a href="../二级行业指数/500医药.html">500医药</a></li>
                        <li><a href="../二级行业指数/500信息.html">500信息</a></li>
                        <li><a href="../二级行业指数/300银行.html">300银行</a></li>
                        <li><a href="../二级行业指数/300地产.html">300地产</a></li>
                        <li><a href="../二级行业指数/300运输.html">300运输</a></li>
                        <li><a href="../二级行业指数/300银行.html">300银行</a></li>
                        <li><a href="../二级行业指数/300地产.html">300地产</a></li>
                        <li><a href="../二级行业指数/300运输.html">300运输</a></li>
                        <li><a href="../二级行业指数/800地产.html">800地产</a></li>
                    </ul>
                </li>
            </ul>
        </nav>
    </div>
</header>
</body>
</html>
'''