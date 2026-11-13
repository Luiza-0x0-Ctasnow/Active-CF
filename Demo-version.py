#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Active-CF: Simple & Direct Recommendation Engine with Vector Radius Control
License: MIT
"""

from math import sqrt

# 内置测试数据集（电影评分网关：用户 -> {物品: 评分}）
dataset = {
    'Toby': {'Snakes on a Plane': 4.5, 'Snakes on a Plane 2': 4.0, 'Superman Returns': 1.0, 'You, Me and Dupree': 4.0},
    'Lisa': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5},
    'Gene': {'Snakes on a Plane': 3.0, 'Superman Returns': 4.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0},
    'Mick': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'The Night Listener': 3.0}
}

def pearson_correlation(p1, p2):
    """计算两个用户的皮尔逊相似度"""
    both = [item for item in dataset[p1] if item in dataset[p2]]
    n = len(both)
    if n == 0: return 0
    
    sum1 = sum(dataset[p1][item] for item in both)
    sum2 = sum(dataset[p2][item] for item in both)
    sum1_sq = sum(pow(dataset[p1][item], 2) for item in both)
    sum2_sq = sum(pow(dataset[p2][item], 2) for item in both)
    product_sum = sum(dataset[p1][item] * dataset[p2][item] for item in both)

    numerator = product_sum - (sum1 * sum2 / n)
    denominator = sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))
    
    return 0 if denominator == 0 else numerator / denominator


class ActiveSimilarityEngine:
    def __init__(self, data=dataset):
        self.dataset = data
        self.radius = {}       # 用户的向量搜索半径 (默认 1.0)
        self.weights = {}      # 对特定用户的加权/屏蔽 { user: { peer: weight } }

    def set_explorer_mode(self, user, radius_multiplier):
        """调节宏观探索半径：>1.0 开启探索/打破茧房，<1.0 锁定核心圈子"""
        self.radius[user] = max(0.1, radius_multiplier)

    def boost_peer(self, user, peer, weight):
        """调节微观偏好：手动加权或屏蔽某个相似用户（如 weight=2.0 强力采纳，0.1 屏蔽）"""
        if user not in self.weights: self.weights[user] = {}
        self.weights[user][peer] = weight

    def get_similar_users(self, user, top_n=3):
        """获取相似用户列表（融合了向量半径与主动干预）"""
        r_factor = self.radius.get(user, 1.0)
        scores = []

        for other in self.dataset:
            if other == user: continue
            base = pearson_correlation(user, other)
            peer_w = self.weights.get(user, {}).get(other, 1.0)
            
            # 最终得分 = 基础相似度 × 向量半径 × 主动意图权重
            final_score = base * r_factor * peer_w
            scores.append((final_score, other))

        scores.sort(key=lambda x: x[0], reverse=True)
        return scores[:top_n]


# ==================== 快速测试 ====================
if __name__ == "__main__":
    engine = ActiveSimilarityEngine()
    
    print("1. 默认状态下的相似用户:", engine.get_similar_users('Toby'))
    
    # 场景模拟：用户 Toby 开启探索模式，并主动喜欢 Gene 的品味、屏蔽 Mick
    engine.set_explorer_mode('Toby', 2.0)  # 放大搜索半径
    engine.boost_peer('Toby', 'Gene', 2.5) # 强推 Gene
    engine.boost_peer('Toby', 'Mick', 0.1) # 降权 Mick
    
    print("2. 调整雷达半径与主动干预后:", engine.get_similar_users('Toby'))
