import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

class GasAnalyzer:
    def __init__(self):
        self.plt = plt
        sns.set_theme()  # 使用seaborn的主题
        
    def create_comparison_bar(self, methods, costs, title, filename):
        """创建简单的柱状图比较"""
        plt.figure(figsize=(8, 6))
        plt.bar(methods, costs)
        plt.title(title)
        plt.ylabel('Gas Cost (units)')
        plt.grid(True, alpha=0.3)
        plt.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
        plt.close()
        
    def create_version_comparison(self, methods, data_dict, title, filename):
        """创建版本对比的分组柱状图"""
        x = np.arange(len(methods))
        width = 0.4  # 加宽单个柱子
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # 动态创建柱状图
        bars = []
        for i, (label, values) in enumerate(data_dict.items()):
            position = x
            bar = ax.bar(position, values, width, label=label)
            bars.append(bar)
            
        # 自定义图表
        ax.set_ylabel('Gas Cost')
        ax.set_title(title)
        ax.set_xticks(x)
        ax.set_xticklabels(methods)
        ax.set_xlim(-0.6, len(methods) - 0.4)  # 让柱子更靠近中间
        ax.set_ylim(31000, 31700)  # 根据数据范围调整
        ax.legend(loc='upper right')
        
        # 添加数值标签
        for bar in bars:
            self._add_value_labels(ax, bar)
            
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # 确保figures目录存在
        os.makedirs('./figures', exist_ok=True)
        plt.savefig(f'./figures/{filename}.pdf', bbox_inches='tight')
        plt.close()
        
    def _add_value_labels(self, ax, rects):
        """添加数值标签的辅助函数"""
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{int(height)}',
                        xy=(rect.get_x() + rect.get_width()/2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', 
                        rotation=90)

    def create_version_comparison_zoomed(self, methods, data_dict, title, filename):
        """创建放大视图的版本对比图"""
        x = np.arange(len(methods))
        width = 0.2
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), height_ratios=[1, 3])
        
        # 动态创建柱状图
        bars1, bars2 = [], []
        for i, (label, values) in enumerate(data_dict.items()):
            position = x + (i - len(data_dict)/2 + 0.5) * width
            # 完整视图
            bar1 = ax1.bar(position, values, width, label=label)
            bars1.append(bar1)
            # 放大视图
            bar2 = ax2.bar(position, values, width, label=label)
            bars2.append(bar2)
        
        # 设置两个子图的y轴范围
        ax1.set_ylim(90000, 105000)  # 显示异常值
        ax2.set_ylim(23000, 24000)   # 显示主要数据范围
        
        # 自定义图表
        for ax in [ax1, ax2]:
            ax.set_ylabel('Gas Cost')
            ax.set_xticks(x)
            ax.set_xticklabels(methods)
            ax.legend()
            ax.grid(True, alpha=0.3)
        
        ax1.spines['bottom'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax1.xaxis.tick_top()
        ax2.xaxis.tick_bottom()
        
        plt.title(title)
        plt.tight_layout()
        # 创建figures目录（如果不存在）
        if not os.path.exists('figures'):
            os.makedirs('figures')
        plt.savefig(f'figures/{filename}.pdf', bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    analyzer = GasAnalyzer()
    

    methods = ['assert', 'require', 'revert']
    data1 = {
        '0.7.0 Success': [23424, 23447, 23491],
        '0.7.0 Failure': [100000, 23494, 23538],
        '0.8.0 Success': [23543, 23565, 23609],
        '0.8.0 Failure': [23383, 23662, 23706]
    }
    # 创建放大视图的版本对比
    analyzer.create_version_comparison_zoomed(methods, data1,
                                           '···too long to be omitted···',
                                           'version_comparison')
    
    # Modifier vs Direct comparison
    # methods = ['Direct', 'Modifier']
    # data = {
    #     'Success': [23542, 23586],
    #     'Failure': [23639, 23683]
    # }
    # analyzer.create_version_comparison(methods, data,
    #                                 'Gas Consumption: Direct vs Modifier Validation',
    #                                 'modifier_comparison')

    
    # Transfer methods comparison
    # methods = ['Transfer', 'Send', 'Call']
    # data = {
    #     'Gas Cost': [31314, 31491, 31375]
    # }
    # analyzer.create_version_comparison(methods, data,
    #                                 'Gas Consumption: ETH Transfer Methods Comparison',
    #                                 'transfer_comparison')

    # Arithmetic operations comparison
    # methods = ['Native', 'SafeMath', 'Unchecked']
    # data = {
    #     'Gas Cost': [22292, 22376, 22091]
    # }
    # analyzer.create_version_comparison(methods, data,
    #                                 'Gas Consumption: Arithmetic Operations Comparison',
    #                                 'arithmetic_comparison')