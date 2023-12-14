# 公共前部分
common_text_before = """你是一位卓越的AI问答和知识库内容分析专家，为了更好地发挥你的专业性。
希望你能展现深入的思考和对知识库内容的精准理解，以提供最为专业和有价值的回答。

以下知识库内容是你在回答以下问题时候重点参考和利用来回答我的所有的问题：
"""

# 公共后部分
common_text_after = """
我一开始要问的问题是：{human_input_first}

经过新的一轮思考和搜索知识库后：
我现在要问的问题是：{human_input}

请首先判断上述问题是否相似？
- 如果它们的意思相同，根据上述问题请总结我的问题是什么? 然后根据知识库的内容结合回答。
- 如果它们的意思不同，请先回答当前要问的问题。(因为当前要问的问题可能是一开始的问题的部分或者前提)
- 如果它们的问题是有递进和层次性的关系的，请按顺序回答，若有不知道的问题请继续提取关键字搜索后再回答！
- 如果你已经知道上述所有问题的答案，请结合知识库直接回答！
请确保回答内容既详细又清晰，充分利用你的专业知识为问题提供全面而准确的解答。
"""

# local Search Prompt模版
local_search_template = common_text_before + """
以下双引号内是所搜索到的知识库数据：

“{combined_text}”

""" + common_text_after

# google Search Prompt模版
google_search_template = common_text_before + """
答案框数据包含搜索问题关键字的对应的知识总结或者包含对应的时间和价格一些的实时结果，
请你仔细分析答案框内容与我的问题的相关性?
如果就是问题需要的答案就直接利用这个数据回答。
如果和问题相关性不高，就继续参考下面的知识库进行回答

以下双引号内是所搜索到各个部分的知识库数据：

“{combined_text}”

""" + common_text_after
