// // 基于准备好的dom，初始化echarts实例
// var myChart = echarts.init(document.getElementById('main'));

// // 指定图表的配置项和数据
// var option = {
//     title: {
//         text: 'ECharts 入门示例'
//     },
//     tooltip: {},
//     legend: {
//         data: ['销量']
//     },
//     xAxis: {
//         data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子', '這啥']
//     },
//     yAxis: {},
//     series: [
//         {
//             name: '销量',
//             type: 'line',
//             //bar,line,
//             data: [5, 20, 36, 10, 10, 20, 21]
//         }
//     ]
// };

// // 使用刚指定的配置项和数据显示图表。
// myChart.setOption(option);





const chart1 = echarts.init(document.querySelector('#pm25_scrip'));
const chart2 = echarts.init(document.querySelector('#pm25_six'));
const chart3 = echarts.init(document.querySelector('#county_pm25'));

// 自適應視窗(自動縮放)
window.onresize = function () {
    chart1.resize();
    chart2.resize();
    chart3.resize();
}

// 讀取縣市選項
document.querySelector('#county_select_b').addEventListener('click', () => {
    const county = document.querySelector('#county_select').value;
    // 記得.value
    if (county !== "") {
        drawcountypm25(county);
    }
});



// 網頁準備好後，進行渲染
$(document).ready(() => {
    drawPM25Chart();
    drawsixpm25();
    drawcountypm25('新北市');
});

// 繪圖縣市圖表
function drawcountypm25(county) {
    $.ajax(
        {
            url: `/county-pm25/${county}`,
            type: 'POST',
            dataType: 'json',
            //dataType  T 一定要大寫
            success: (datas) => {
                console.log(datas)
                const option = {
                    title: {
                        text: county
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['PM2.5']
                    },
                    xAxis: {
                        data: datas['sites']
                    },
                    yAxis: {},
                    series: [
                        {
                            showBackground: true,
                            itemStyle: {
                                // Styles for normal state.
                                normal: {
                                    color: '#5a9be0'
                                },
                                // Styles for emphasis state.
                                emphasis: {
                                    color: '#103266'
                                }
                            },
                            name: 'pm2.5',
                            type: 'bar',
                            data: datas['pm25']
                        }
                    ]


                }
                chart3.setOption(option);
            }

        }
    )
}

// 繪圖六都圖表
function drawsixpm25() {
    $.ajax(
        {
            url: '/six-pm25',
            type: 'POST',
            dataType: 'json',
            //dataType  T 一定要大寫
            success: (datas) => {
                console.log(datas)
                const option = {
                    title: {
                        text: 'PM2.5全台圖'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['PM2.5']
                    },
                    xAxis: {
                        data: datas['citys']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'pm2.5',
                            type: 'bar',
                            data: datas['pm25']
                        }
                    ]


                }
                chart2.setOption(option);
            }

        }
    )
}




// 繪圖全部圖表
function drawPM25Chart() {
    $.ajax(
        {
            url: '/pm25-data',
            type: 'POST',
            dataType: 'json',
            //dataType  T 一定要大寫
            success: (datas) => {
                console.log(datas)
                const option = {
                    title: {
                        text: 'PM2.5全台圖'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['PM2.5']
                    },
                    xAxis: {
                        data: datas['sites']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'pm2.5',
                            type: 'bar',
                            data: datas['pm25_da']
                        }
                    ]


                }
                $('#highest_pm25_site').text(datas['highest'][0]);
                $('#highest_pm25_vaule').text(datas['highest'][1]);
                $('#lowest_pm25_site').text(datas['lowest'][0]);
                $('#lowest_pm25_value').text(datas['lowest'][1]);
                $('#date').text(datas['time']);

                //document.querySelector('highest_pm25_site').innerText(datas['highest'][0])

                console.log(chart1);
                console.log(option);

                chart1.setOption(option);
            }

        }
    )
}


