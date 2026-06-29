from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "reference_archive"
CSV_PATH = ROOT / "reference_index_bilingual.csv"
LEGACY_CSV_PATH = ROOT / "reference_index.csv"
TABLE_PATH = ROOT / "reference_table_bilingual.md"


OVERRIDES = {
    "core_umbrella_2022_leichsenring": {
        "clinical_scene_zh": "先搭总图时看这篇。它适合回答一个基础问题：不同障碍通常对应哪些治疗路线。",
        "abstract_summary_zh": "总览文献。结论很直接：心理治疗整体有效，但不同流派各有适用面，没有一把通吃的方案。",
        "why_included_zh": "用它做全局底图。",
        "practical_takeaway_zh": "先定方向，再回到具体障碍的专项综述。",
    },
    "core_cbt_2025_cuijpers": {
        "clinical_scene_zh": "适合症状结构比较清楚的个案：回避、灾难化、反复检查、创伤后退缩、行为循环明显。",
        "abstract_summary_zh": "CBT 总图。覆盖面很广，抑郁、焦虑、PTSD、OCD 和部分饮食障碍都有稳定支持。",
        "why_included_zh": "做 CBT 板块时，这篇足够当主干。",
        "practical_takeaway_zh": "能拆成想法、情绪、行为链条的问题，通常都能用 CBT 讲明白。",
    },
    "core_anxiety_cbt_2018_carpenter": {
        "clinical_scene_zh": "适合长期担忧、过度警觉、反复回避、不断求确认的焦虑场景。",
        "abstract_summary_zh": "焦虑专项元分析。即便用更严格的安慰剂对照，CBT 仍然有中等效应。",
        "why_included_zh": "补焦虑板块的硬证据。",
        "practical_takeaway_zh": "焦虑的核心常在回避循环，暴露通常绕不过去。",
    },
    "core_gad_nma_2023_papola": {
        "clinical_scene_zh": "适合那种一直担心、停不下来、脑子总在预演坏结果的人。",
        "abstract_summary_zh": "GAD 专项比较。短期看第三波 CBT、传统 CBT、放松训练都有效；长期结果里，CBT 最稳。",
        "why_included_zh": "GAD 需要单独看。",
        "practical_takeaway_zh": "GAD 的关键在担忧本身的维持机制。",
    },
    "core_social_anxiety_nma_2025_hong": {
        "clinical_scene_zh": "适合害怕评价、事后反刍重、社交回避明显的场景。",
        "abstract_summary_zh": "社交焦虑专项比较。CBT 仍然最强，非 CBT 里动力学治疗也有位置。",
        "why_included_zh": "把焦虑板块细分到社交焦虑，不再笼统写成一类。",
        "practical_takeaway_zh": "社交焦虑要进场景，不能只在纸上谈理解。",
    },
    "core_depression_nma_2021_cuijpers": {
        "clinical_scene_zh": "适合需要比较多条抑郁治疗路线时使用，尤其是在不想只盯一种流派的时候。",
        "abstract_summary_zh": "抑郁横向比较文献。几种主要心理治疗都有效，差异没有很多人想的那么大。",
        "why_included_zh": "抑郁板块的对照底盘。",
        "practical_takeaway_zh": "选治疗时，病人的维持机制和偏好常比流派名头更重要。",
    },
    "core_ipt_2016_cuijpers": {
        "clinical_scene_zh": "适合情绪问题和失恋、丧亲、迁居、婚育、照护压力直接连在一起的个案。",
        "abstract_summary_zh": "IPT 的主战场是抑郁，围产期和关系事件相关场景尤其突出。",
        "why_included_zh": "它能把‘关系事件型抑郁’单独拎出来。",
        "practical_takeaway_zh": "问题如果跟关系事件同步恶化，IPT 往往很贴题。",
    },
    "core_pdt_2023_wienicke": {
        "clinical_scene_zh": "适合反复陷进同一种关系脚本、情感表达受阻、防御明显的人。",
        "abstract_summary_zh": "动力学治疗在抑郁里有稳定疗效。这篇用的是个体数据级别的综述。",
        "why_included_zh": "动力学板块的核心证据之一。",
        "practical_takeaway_zh": "症状总在重复同一种命运时，动力学视角很有用。",
    },
    "core_ptsd_exposure_2022_wootton": {
        "clinical_scene_zh": "适合创伤后回避强、触发后失控快、警觉性高的人群。",
        "abstract_summary_zh": "PTSD 里的暴露治疗证据很扎实。重点在于重建对创伤线索的加工。",
        "why_included_zh": "PTSD 板块里，暴露证据必须单列。",
        "practical_takeaway_zh": "创伤治疗里，回避既是保护，也是维持因素。",
    },
    "core_ptsd_psychological_2015_lewis": {
        "clinical_scene_zh": "适合先看 PTSD 总图，再决定切入技术的时候。",
        "abstract_summary_zh": "PTSD 总览文献。创伤聚焦治疗长期占一线。",
        "why_included_zh": "给 PTSD 板块补总图。",
        "practical_takeaway_zh": "先看全局，再选暴露、认知加工或其他创伤聚焦方案。",
    },
    "core_ocd_erp_2021_jonsson": {
        "clinical_scene_zh": "适合反复检查、清洗、确认、仪式行为明显的强迫症场景。",
        "abstract_summary_zh": "OCD 的技术核心就是 ERP。这篇文献讲得很清楚。",
        "why_included_zh": "强迫症最需要把技术名真正落到操作上。",
        "practical_takeaway_zh": "不碰仪式化行为，很多洞察都落不了地。",
    },
    "core_dbt_bpd_2021_kothgassner": {
        "clinical_scene_zh": "适合情绪冲得很快、自伤冲动高、关系剧烈摆动的场景。",
        "abstract_summary_zh": "DBT 在减少自伤和压低高强度负性情绪上有明确支持。",
        "why_included_zh": "DBT 板块的核心证据。",
        "practical_takeaway_zh": "DBT 的长处在训练，不在安慰。",
    },
    "core_bpd_psychotherapies_2017_cristea": {
        "clinical_scene_zh": "适合比较 BPD 的不同治疗路线，也适合跳出 DBT 单一路径来看。",
        "abstract_summary_zh": "BPD 不只有 DBT。多种结构化治疗都有证据，只是强弱和稳定性不同。",
        "why_included_zh": "给人格障碍板块留出更完整的视野。",
        "practical_takeaway_zh": "治疗选择要看风险、资源和来访者能否进入长期结构化工作。",
    },
    "core_family_schizophrenia_2022_rodolico": {
        "clinical_scene_zh": "适合高情绪表达、高照护负担、复发和家庭压力绑得很紧的场景。",
        "abstract_summary_zh": "家庭干预对精神分裂症复发预防有硬证据支持。",
        "why_included_zh": "系统治疗在这个适应症上很强，必须单列。",
        "practical_takeaway_zh": "这类个案里，家庭气候本身就是治疗变量。",
    },
    "core_family_anorexia_2024_murray": {
        "clinical_scene_zh": "适合青春期厌食、体重下降、家庭高度卷入又容易冲突升级的场景。",
        "abstract_summary_zh": "青少年厌食症里，家庭治疗通常是主轴。",
        "why_included_zh": "补强系统治疗在厌食症中的经典适应症。",
        "practical_takeaway_zh": "患者还深嵌家庭系统时，单人治疗常常不够。",
    },
    "core_perinatal_cbt_2022_li": {
        "clinical_scene_zh": "适合孕期或产后因角色变化、睡眠剥夺、照护压力而恶化的情绪问题。",
        "abstract_summary_zh": "围产期 CBT 证据稳定，抑郁、焦虑和压力都能覆盖到。",
        "why_included_zh": "把抑郁板块扩到真实高频的围产期场景。",
        "practical_takeaway_zh": "围产期干预要同时看认知、节律和支持系统。",
    },
    "guideline_nice_2022_depression": {
        "clinical_scene_zh": "适合把研究证据转成临床路径和优先级时使用。",
        "abstract_summary_zh": "NICE 的价值在排序。它把证据转成了能执行的治疗路径。",
        "why_included_zh": "做方案排序时要回到指南。",
        "practical_takeaway_zh": "知道有证据和知道先做什么，是两回事。",
    },
    "guideline_apa_2019_depression": {
        "clinical_scene_zh": "适合比较不同年龄层抑郁治疗推荐时使用。",
        "abstract_summary_zh": "APA 指南更强调年龄分层，适合和 NICE 对照看。",
        "why_included_zh": "补足美国体系下的年龄维度。",
        "practical_takeaway_zh": "儿童、成人、老年抑郁不能用同一套优先级硬套。",
    },
    "support_ataglance_2024": {
        "clinical_scene_zh": "适合快速建立治疗地图，不适合直接当终局证据。",
        "abstract_summary_zh": "导航文献。用来定方向很好，用来下结论不够。",
        "why_included_zh": "检索入口好用。",
        "practical_takeaway_zh": "先拿它找路，再回到元分析和指南。",
        "key_techniques_zh": "概览级建议，侧重导航",
    },
    "theory_shedler_2010": {
        "clinical_scene_zh": "适合理解动力学治疗在公共讨论里为什么总被误读。",
        "abstract_summary_zh": "理论入口文。能帮助你看懂动力学的自我辩护逻辑。",
        "why_included_zh": "留作理论补充，不放进核心证据排序。",
        "practical_takeaway_zh": "拿它讲流派可以，拿它单扛疗效不行。",
    },
    "official_dbt_faq": {
        "clinical_scene_zh": "适合想快速弄清 DBT 结构和四大技能模块的时候。",
        "abstract_summary_zh": "说明文。讲结构很清楚，但不属于疗效证据。",
        "why_included_zh": "用于概念澄清。",
        "practical_takeaway_zh": "把它当说明书，不要当元分析。",
    },
}


def load_rows() -> list[dict]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def save_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def update_rows(rows: list[dict]) -> list[dict]:
    for row in rows:
        patch = OVERRIDES.get(row["citation_id"])
        if patch:
            row.update(patch)
    return rows


def write_table(rows: list[dict]) -> None:
    lines = [
        "# Bilingual Reference Table",
        "",
        "| ID | 流派 | 适应症 | 证据类型 | 引用量 | OA | Q/Rank | 摘要总结 |",
        "| --- | --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for row in rows:
        qrank = "-"
        if row.get("journal_best_quartile") or row.get("journal_rank_2025"):
            qrank = f"{row.get('journal_best_quartile', '-') or '-'} / {row.get('journal_rank_2025', '-') or '-'}"
        lines.append(
            f"| {row['citation_id']} | {row['therapy_modality_zh']} | {row['indication_zh']} | {row['study_design_zh']} | {row['citation_count_epmc'] or '-'} | {row['is_open_access'] or '-'} | {qrank} | {row['abstract_summary_zh']} |"
        )
    TABLE_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_cards(rows: list[dict]) -> None:
    for row in rows:
        card_dir = ROOT / row["folder"] / row["subfolder"]
        card_path = card_dir / f"{row['year']}_{row['citation_id']}.md"
        text = f"""# {row['title_en']}

## 中文标题

{row['title_zh']}

## 基本信息

- citation_id: {row['citation_id']}
- authors: {row['authors']}
- year: {row['year']}
- journal: {row['journal']}
- study_design: {row['study_design_zh']}
- doi: {row['doi']}
- pmid: {row['pmid']}
- pmcid: {row['pmcid']}

## 流派与适应症

- 流派: {row['therapy_modality_zh']}
- 适应症: {row['indication_zh']}
- 推荐等级: {row['recommendation_level_zh']}
- 核心证据: {row['can_be_used_as_core_evidence']}

## 常见场景

{row['clinical_scene_zh']}

## 核心技术

- EN: {row['key_techniques_en']}
- 中文: {row['key_techniques_zh']}

## 英文摘要

{row['abstract_en'] or 'No abstract captured.'}

## 中文摘要总结

{row['abstract_summary_zh']}

## 收录理由

{row['why_included_zh']}

## 实操提醒

{row['practical_takeaway_zh']}

## 开放获取与全文

- primary_url: {row['primary_url']}
- best_free_fulltext_url: {row['best_free_fulltext_url']}
- all_fulltext_urls: {row['all_fulltext_urls']}
- local_pmc_pdf: {row['local_pmc_pdf']}
- is_open_access: {row['is_open_access']}
- in_pmc: {row['in_pmc']}
- has_pdf: {row['has_pdf']}
- auth_manuscript: {row['auth_manuscript']}

## 引用量与期刊信息

- article_citation_count: {row['citation_count_epmc']}
- citation_count_source: {row['citation_count_source']}
- citation_snapshot_date: {row['citation_count_snapshot_date']}
- journal_publisher: {row['journal_publisher']}
- journal_best_quartile: {row['journal_best_quartile']}
- journal_sjr_2025: {row['journal_sjr_2025']}
- journal_h_index_2025: {row['journal_h_index_2025']}
- journal_rank_2025: {row['journal_rank_2025']}
- journal_impact_score_2024_2025: {row['journal_impact_score_2024_2025']}
- journal_scope: {row['journal_scope']}
- journal_metrics_source: {row['journal_metrics_source']}
- journal_metrics_url: {row['journal_metrics_url']}
"""
        card_path.write_text(text, encoding="utf-8")


def main() -> None:
    rows = update_rows(load_rows())
    save_csv(CSV_PATH, rows)
    save_csv(LEGACY_CSV_PATH, rows)
    write_table(rows)
    write_cards(rows)


if __name__ == "__main__":
    main()
