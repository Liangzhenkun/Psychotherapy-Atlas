from __future__ import annotations

import csv
import html
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent / "reference_archive"
PDF_DIR = ROOT / "_downloads_pmc_pdfs"
OA_DIR = ROOT / "_open_access_links"
SNAPSHOT_DATE = "2026-06-26"


SOURCE_DEFS = [
    {
        "citation_id": "core_umbrella_2022_leichsenring",
        "query": {"type": "doi", "value": "10.1002/wps.20941"},
        "folder": "01_core_evidence",
        "subfolder": "general_psychotherapy",
        "title_zh": "成人精神障碍中心理治疗与药物治疗的疗效：伞形综述与近期元分析再评价",
        "study_design_zh": "伞形综述",
        "therapy_modality_en": "Cross-modality psychotherapy",
        "therapy_modality_zh": "跨流派心理治疗总览",
        "indication_en": "Adult mental disorders",
        "indication_zh": "成人常见精神障碍总体图谱",
        "clinical_scene_zh": "适合用来搭建总地图：当你想先知道抑郁、焦虑、人格、精神病性问题分别更常对应哪些治疗思路时，先看这类总览。",
        "key_techniques_en": "Cross-modality overview",
        "key_techniques_zh": "总览型比较，不聚焦单一技术",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "这篇文章不是在找唯一最强流派，而是在高层证据上确认：心理治疗总体有效，但不同流派在不同障碍上的优势分布并不相同。它适合用来作为整个知识系统的总起点。",
        "why_included_zh": "作为总纲级证据，用于支撑整套‘流派-技术-适应症’框架。",
        "practical_takeaway_zh": "先用它判断大方向，再回到具体诊断的专项综述做细化。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_cbt_2025_cuijpers",
        "query": {"type": "pmid", "value": "40238104"},
        "folder": "01_core_evidence",
        "subfolder": "cbt",
        "title_zh": "认知行为治疗用于成人精神障碍：统一系列元分析",
        "study_design_zh": "统一方法框架下的系列元分析",
        "therapy_modality_en": "CBT",
        "therapy_modality_zh": "认知行为治疗",
        "indication_en": "Depression, anxiety disorders, PTSD, OCD, eating disorders, psychotic and bipolar disorders",
        "indication_zh": "抑郁、焦虑谱系、PTSD、OCD、饮食障碍，以及部分双相/精神病性问题",
        "clinical_scene_zh": "适用于自动化负性思维强、回避明显、症状和行为循环容易观察的人群，例如反复拖延、惊恐回避、社交恐惧、反复检查或创伤后回缩。",
        "key_techniques_en": "Cognitive restructuring; exposure; behavioral activation; behavioral experiments; problem solving",
        "key_techniques_zh": "认知重构、暴露、行为激活、行为实验、问题解决",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "该研究以统一方法重新汇总成人精神障碍中的 CBT 随机试验，显示 CBT 对抑郁、焦虑、PTSD、OCD 和部分饮食障碍具有稳定疗效。不同对照条件会影响效应量大小，但 CBT 的广覆盖优势非常明确。",
        "why_included_zh": "这是当前最适合做 CBT 总图的核心文献之一。",
        "practical_takeaway_zh": "当症状可被拆解为‘想法-情绪-行为’链条时，CBT 往往最容易转成实操。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_anxiety_cbt_2018_carpenter",
        "query": {"type": "pmid", "value": "29451967"},
        "folder": "01_core_evidence",
        "subfolder": "anxiety",
        "title_zh": "CBT 对焦虑及相关障碍的疗效：随机安慰剂对照试验元分析",
        "study_design_zh": "元分析",
        "therapy_modality_en": "CBT",
        "therapy_modality_zh": "认知行为治疗",
        "indication_en": "Anxiety and related disorders",
        "indication_zh": "焦虑障碍及相关障碍",
        "clinical_scene_zh": "适合长期担忧、灾难化预测、回避、寻求保证、过度警觉明显的来访者。",
        "key_techniques_en": "Cognitive restructuring; exposure; inhibitory learning; response prevention",
        "key_techniques_zh": "认知重构、暴露、抑制性学习、反应预防",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "这篇研究用更严格的安慰剂对照试验来检验 CBT 对焦虑相关障碍的真实效果，结果依然支持 CBT 显著优于对照。它有助于降低‘只是等时间过去也会好’这类解释带来的误判。",
        "why_included_zh": "补足 CBT 在焦虑领域的高质量专项证据。",
        "practical_takeaway_zh": "如果问题核心是恐惧预期和回避循环，暴露类技术通常应进入方案中心。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_gad_nma_2023_papola",
        "query": {"type": "pmid", "value": "37851421"},
        "folder": "01_core_evidence",
        "subfolder": "anxiety",
        "title_zh": "成人广泛性焦虑障碍的心理治疗：系统综述与网络元分析",
        "study_design_zh": "系统综述与网络元分析",
        "therapy_modality_en": "Multiple psychotherapies for GAD",
        "therapy_modality_zh": "广泛性焦虑的多流派心理治疗",
        "indication_en": "Generalized anxiety disorder in adults",
        "indication_zh": "成人广泛性焦虑障碍",
        "clinical_scene_zh": "适合那种‘一直担心、停不下来、睡不着、脑子总在做最坏打算’的广泛性焦虑场景。",
        "key_techniques_en": "CBT packages; cognitive therapy; applied relaxation; worry exposure",
        "key_techniques_zh": "CBT 套件、认知治疗、应用性放松、担忧暴露",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "该网络元分析聚焦 GAD，帮助区分哪些心理治疗在长期担忧型焦虑中更有优势。对于‘担忧失控’而非单次惊恐发作型问题，它特别有实用价值。",
        "why_included_zh": "GAD 的临床表现和 panic/social anxiety 不同，需要专项证据支持。",
        "practical_takeaway_zh": "GAD 干预的重点常在于减少对担忧本身的依赖，而不只是简单放松。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_social_anxiety_nma_2025_hong",
        "query": {"type": "pmid", "value": "40023260"},
        "folder": "01_core_evidence",
        "subfolder": "anxiety",
        "title_zh": "成人社交焦虑障碍的心理治疗：系统综述与贝叶斯网络元分析",
        "study_design_zh": "系统综述与贝叶斯网络元分析",
        "therapy_modality_en": "Psychotherapies for social anxiety disorder",
        "therapy_modality_zh": "社交焦虑障碍的心理治疗",
        "indication_en": "Social anxiety disorder in adults",
        "indication_zh": "成人社交焦虑障碍",
        "clinical_scene_zh": "适合‘别人会怎么看我’主导、表现前极度紧张、事后反刍很重、社交回避明显的场景。",
        "key_techniques_en": "Exposure; cognitive restructuring; attention training; social skills rehearsal",
        "key_techniques_zh": "暴露、认知重构、注意训练、社交技能演练",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "社交焦虑与广泛性焦虑并不相同，这篇新近网络元分析更适合用来比较社交焦虑中的不同治疗形式。它有利于把‘害怕别人评价’这一核心维持机制和一般性担忧区分开。",
        "why_included_zh": "让焦虑板块不只停留在笼统 CBT，而是能细分到社交焦虑这一高频场景。",
        "practical_takeaway_zh": "社交焦虑最需要的往往不是解释，而是逐步进入会引发评价恐惧的真实情境。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_depression_nma_2021_cuijpers",
        "query": {"type": "doi", "value": "10.1002/wps.20860"},
        "folder": "01_core_evidence",
        "subfolder": "depression",
        "title_zh": "抑郁的心理治疗：涵盖疗效、可接受性与长期结局的网络元分析",
        "study_design_zh": "网络元分析",
        "therapy_modality_en": "Multiple psychotherapies for depression",
        "therapy_modality_zh": "抑郁的多流派心理治疗",
        "indication_en": "Depression",
        "indication_zh": "抑郁障碍",
        "clinical_scene_zh": "适合精力下降、快感缺失、自我否定、活动回缩、关系退避等抑郁图景，但又想比较不止一种治疗路线时。",
        "key_techniques_en": "Behavioral activation; CBT; IPT; problem-solving therapy; psychodynamic approaches",
        "key_techniques_zh": "行为激活、CBT、IPT、问题解决治疗、动力学取向",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "这篇研究最大的价值是横向比较抑郁治疗中的主要流派，不只看短期疗效，还考虑可接受性和长期结果。它适合回答‘同样是抑郁，为什么不同人适合不同路线’。",
        "why_included_zh": "是抑郁领域做跨流派比较时最值得保留的关键来源之一。",
        "practical_takeaway_zh": "抑郁治疗不要只问哪种最强，更要问症状是由回避、关系丧失还是人格模式在维持。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_ipt_2016_cuijpers",
        "query": {"type": "doi", "value": "10.1176/appi.ajp.2015.15091141"},
        "folder": "01_core_evidence",
        "subfolder": "ipt",
        "title_zh": "人际心理治疗用于精神健康问题：综合元分析",
        "study_design_zh": "综合元分析",
        "therapy_modality_en": "IPT",
        "therapy_modality_zh": "人际心理治疗",
        "indication_en": "Depression and selected mental health problems",
        "indication_zh": "抑郁及部分与关系事件相关的精神健康问题",
        "clinical_scene_zh": "适合因失恋、丧亲、迁居、婚育、照护压力或角色转换而明显恶化的情绪问题。",
        "key_techniques_en": "Grief work; role transition work; interpersonal disputes; social support rebuilding",
        "key_techniques_zh": "哀伤工作、角色转变工作、人际争端分析、社会支持重建",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "IPT 的强项在于把症状放回关系事件和社会角色变化中理解。对抑郁尤其是围产期、哀伤和关系失衡相关的抑郁场景，这类证据非常关键。",
        "why_included_zh": "它能帮助你把‘关系事件型抑郁’从一般抑郁里区分出来。",
        "practical_takeaway_zh": "如果来访者的问题和关键关系事件高度同步，IPT 往往比单纯讨论认知更贴近现场。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_pdt_2023_wienicke",
        "query": {"type": "pmid", "value": "36958077"},
        "folder": "01_core_evidence",
        "subfolder": "psychodynamic",
        "title_zh": "短程心理动力学治疗抑郁的疗效与调节因素：个体参与者数据系统综述与元分析",
        "study_design_zh": "个体参与者数据系统综述与元分析",
        "therapy_modality_en": "Psychodynamic therapy / STPP",
        "therapy_modality_zh": "短程心理动力学治疗",
        "indication_en": "Depression",
        "indication_zh": "抑郁障碍，尤其伴随关系重演和防御结构者",
        "clinical_scene_zh": "适合那种总在亲密关系、权威关系或依赖/疏离之间反复卡住的人，症状背后常有重复性关系脚本。",
        "key_techniques_en": "Clarification; confrontation; interpretation; defense analysis; affect focus; transference work",
        "key_techniques_zh": "澄清、对抗、解释、防御分析、情感聚焦、移情工作",
        "evidence_level": "High",
        "recommendation_level_zh": "中度到强烈推荐",
        "abstract_summary_zh": "这篇 IPD 级别的综述强化了一个结论：动力学治疗不是只会谈过去，它在抑郁治疗中有稳定疗效，且对关系模式和情感组织的理解具有独特价值。",
        "why_included_zh": "是动力学治疗在抑郁领域最该留下的高质量核心证据之一。",
        "practical_takeaway_zh": "当症状总在重复同一种命运时，动力学视角常能看见 CBT 不一定会优先命名的那一层。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_ptsd_exposure_2022_wootton",
        "query": {"type": "pmid", "value": "34954460"},
        "folder": "01_core_evidence",
        "subfolder": "trauma_and_ocd",
        "title_zh": "PTSD 的暴露治疗：元分析",
        "study_design_zh": "元分析",
        "therapy_modality_en": "Exposure therapy for PTSD",
        "therapy_modality_zh": "PTSD 的暴露治疗",
        "indication_en": "PTSD",
        "indication_zh": "创伤后应激障碍",
        "clinical_scene_zh": "适合创伤后回避、闪回、警觉性高、触发后迅速失控的人群，尤其是回避行为维持症状的场景。",
        "key_techniques_en": "Prolonged exposure; trauma processing; imaginal exposure; in vivo exposure",
        "key_techniques_zh": "延长暴露、创伤加工、想象暴露、现实暴露",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "暴露治疗在 PTSD 中长期被认为核心，但很多学习者会担心它是否‘太刺激’。这篇元分析能帮助你把暴露理解为有结构地重建创伤线索加工，而不是简单强迫回忆。",
        "why_included_zh": "用于补强 PTSD 中最关键的技术证据。",
        "practical_takeaway_zh": "创伤治疗里，回避通常既是保护也是维持机制，暴露工作的意义就在这里。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_ptsd_psychological_2015_lewis",
        "query": {"type": "pmid", "value": "26574151"},
        "folder": "01_core_evidence",
        "subfolder": "trauma_and_ocd",
        "title_zh": "成人 PTSD 的心理治疗：系统综述与元分析",
        "study_design_zh": "系统综述与元分析",
        "therapy_modality_en": "Psychological treatments for adult PTSD",
        "therapy_modality_zh": "成人 PTSD 的心理治疗总览",
        "indication_en": "Adult PTSD",
        "indication_zh": "成人 PTSD",
        "clinical_scene_zh": "适合需要先看 PTSD 整体治疗版图，而不是只盯暴露单项技术时。",
        "key_techniques_en": "Trauma-focused CBT; EMDR-related approaches; exposure-based treatments",
        "key_techniques_zh": "创伤聚焦 CBT、EMDR 相关方法、暴露取向治疗",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "相比单项技术综述，这篇更像 PTSD 心理治疗的总图，帮助你理解创伤聚焦治疗为什么会被持续放在一线位置。",
        "why_included_zh": "让 PTSD 板块既有技术专项，又有治疗总览。",
        "practical_takeaway_zh": "先看总图，再决定是从暴露、认知加工还是其他创伤聚焦形式切入。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_ocd_erp_2021_jonsson",
        "query": {"type": "pmid", "value": "33618297"},
        "folder": "01_core_evidence",
        "subfolder": "trauma_and_ocd",
        "title_zh": "结合暴露与反应预防的 CBT 治疗 OCD：随机对照试验系统综述与元分析",
        "study_design_zh": "系统综述与元分析",
        "therapy_modality_en": "CBT with ERP for OCD",
        "therapy_modality_zh": "结合 ERP 的认知行为治疗",
        "indication_en": "Obsessive-compulsive disorder",
        "indication_zh": "强迫症",
        "clinical_scene_zh": "适合反复检查、清洗、确认、内疚式强迫思维和仪式行为明显的场景。",
        "key_techniques_en": "Exposure and response prevention; cognitive restructuring; ritual blocking",
        "key_techniques_zh": "暴露与反应预防、认知重构、仪式阻断",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "OCD 的实操核心不是单纯谈认知，而是 ERP。该综述强调了 ERP 在减少强迫行为和维持循环中的关键作用。",
        "why_included_zh": "强迫症是最需要把‘技术名字’真正落到实操上的障碍之一。",
        "practical_takeaway_zh": "如果不处理仪式化行为，很多口头洞察对 OCD 来说都不够。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_dbt_bpd_2021_kothgassner",
        "query": {"type": "pmid", "value": "34519138"},
        "folder": "01_core_evidence",
        "subfolder": "personality_and_self_harm",
        "title_zh": "DBT 对边缘型人格障碍患者自伤行为与负性情绪的影响：元分析",
        "study_design_zh": "元分析",
        "therapy_modality_en": "DBT",
        "therapy_modality_zh": "辩证行为治疗",
        "indication_en": "Borderline personality disorder with self-harm and intense negative affect",
        "indication_zh": "边缘型人格障碍伴自伤和强烈负性情绪",
        "clinical_scene_zh": "适合情绪像海啸一样来得快去得慢、冲动自伤、关系极端摇摆、事后强烈羞耻的场景。",
        "key_techniques_en": "Chain analysis; distress tolerance; emotion regulation; mindfulness; interpersonal effectiveness",
        "key_techniques_zh": "链式分析、痛苦耐受、情绪调节、正念、人际效能",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "这篇元分析直接对应 DBT 最具代表性的临床价值：降低自伤、自杀相关行为和极端负性情绪。它比泛泛的‘情绪管理’说法更具体也更可信。",
        "why_included_zh": "用于支撑 DBT 在高风险情绪失控场景中的核心地位。",
        "practical_takeaway_zh": "DBT 的关键不是安慰，而是把高风险情绪链条拆开训练。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_bpd_psychotherapies_2017_cristea",
        "query": {"type": "pmid", "value": "28249086"},
        "folder": "01_core_evidence",
        "subfolder": "personality_and_self_harm",
        "title_zh": "边缘型人格障碍的心理治疗疗效：系统综述与元分析",
        "study_design_zh": "系统综述与元分析",
        "therapy_modality_en": "Psychotherapies for BPD",
        "therapy_modality_zh": "边缘型人格障碍的多流派心理治疗",
        "indication_en": "Borderline personality disorder",
        "indication_zh": "边缘型人格障碍",
        "clinical_scene_zh": "适合想比较 DBT、MBT、转移焦点治疗等不同人格障碍治疗路径时。",
        "key_techniques_en": "DBT, MBT, transference-focused and other specialized psychotherapies",
        "key_techniques_zh": "DBT、MBT、移情焦点等人格障碍专项治疗",
        "evidence_level": "High",
        "recommendation_level_zh": "中度到强烈推荐",
        "abstract_summary_zh": "这篇研究的价值在于提醒我们：BPD 不只等于 DBT，虽然 DBT 最有名，但人格障碍治疗还存在多个结构化路线。它适合做视野扩展。",
        "why_included_zh": "避免把人格障碍治疗简化成单一路径。",
        "practical_takeaway_zh": "BPD 的治疗选择要看风险水平、治疗资源和来访者能否进入结构化长期工作。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_family_schizophrenia_2022_rodolico",
        "query": {"type": "doi", "value": "10.1016/S2215-0366(21)00437-5"},
        "folder": "01_core_evidence",
        "subfolder": "family_and_systemic",
        "title_zh": "家庭干预用于精神分裂症复发预防：系统综述与网络元分析",
        "study_design_zh": "系统综述与网络元分析",
        "therapy_modality_en": "Family intervention / systemic family treatment",
        "therapy_modality_zh": "家庭干预 / 系统家庭治疗",
        "indication_en": "Schizophrenia relapse prevention",
        "indication_zh": "精神分裂症复发预防",
        "clinical_scene_zh": "适合高情绪表达家庭、照护耗竭、批评指责多、复发和家庭压力同步上升的场景。",
        "key_techniques_en": "Psychoeducation; communication training; problem solving; relapse warning management",
        "key_techniques_zh": "家庭心理教育、沟通训练、问题解决、复发预警管理",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "这篇研究非常能说明系统/家庭治疗在某些障碍上的真正强项：不是泛泛修关系，而是切实影响复发和再住院风险。",
        "why_included_zh": "家庭治疗最不该被低估的适应症之一就是精神病性障碍复发预防。",
        "practical_takeaway_zh": "对这类个案，改变家庭情绪气候往往和药物管理同样关键。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_family_anorexia_2024_murray",
        "query": {"type": "pmid", "value": "39041682"},
        "folder": "01_core_evidence",
        "subfolder": "family_and_systemic",
        "title_zh": "聚焦进食障碍的家庭治疗用于青少年神经性厌食：系统综述与元分析",
        "study_design_zh": "系统综述与元分析",
        "therapy_modality_en": "Eating-disorder-focused family therapy",
        "therapy_modality_zh": "聚焦进食障碍的家庭治疗",
        "indication_en": "Adolescent anorexia nervosa",
        "indication_zh": "青少年神经性厌食",
        "clinical_scene_zh": "适合青春期体重下降、进食控制、家庭高度卷入又容易冲突升级的场景。",
        "key_techniques_en": "Family-based treatment; caregiver refeeding support; alliance restructuring",
        "key_techniques_zh": "家庭基础治疗、照护者再喂养支持、联盟重建",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "在青少年厌食症中，家庭治疗不是配角而常常是主轴。该研究能帮助你看到‘症状、控制感、亲子关系’如何被放在同一治疗框架中处理。",
        "why_included_zh": "补强系统/家庭治疗在另一个经典适应症中的证据。",
        "practical_takeaway_zh": "当患者仍深嵌家庭系统时，单人治疗常不够。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "core_perinatal_cbt_2022_li",
        "query": {"type": "pmid", "value": "35123346"},
        "folder": "01_core_evidence",
        "subfolder": "perinatal",
        "title_zh": "CBT 对围产期母亲抑郁、焦虑和压力的效果：随机对照试验系统综述与元分析",
        "study_design_zh": "系统综述与元分析",
        "therapy_modality_en": "CBT for perinatal mental health",
        "therapy_modality_zh": "围产期心理健康的 CBT",
        "indication_en": "Perinatal depression, anxiety, and stress",
        "indication_zh": "围产期抑郁、焦虑和压力",
        "clinical_scene_zh": "适合妊娠期或产后因角色变化、睡眠剥夺、照护压力、自责和支持不足而出现情绪问题的场景。",
        "key_techniques_en": "Behavioral activation; cognitive restructuring; stress management; problem solving",
        "key_techniques_zh": "行为激活、认知重构、压力管理、问题解决",
        "evidence_level": "High",
        "recommendation_level_zh": "强烈推荐",
        "abstract_summary_zh": "围产期并不是一般抑郁的简单复制，这篇综述能帮助你把 CBT 放到孕产期特殊生活结构中理解。它尤其适合解释‘角色转换型情绪问题’。",
        "why_included_zh": "把抑郁板块进一步拓展到围产期这一高频实际场景。",
        "practical_takeaway_zh": "围产期干预要同时看到认知、行为节律和社会支持系统。",
        "can_be_used_as_core_evidence": "yes",
    },
    {
        "citation_id": "guideline_nice_2022_depression",
        "query": {"type": "manual", "value": "https://www.nice.org.uk/guidance/ng222"},
        "folder": "02_guidelines",
        "subfolder": "depression",
        "title_en_manual": "Depression in adults: treatment and management (NG222)",
        "title_zh": "成人抑郁：治疗与管理（NICE NG222）",
        "study_design_zh": "临床实践指南",
        "therapy_modality_en": "Guideline-level multimodal recommendations",
        "therapy_modality_zh": "指南级多模式治疗建议",
        "indication_en": "Adult depression",
        "indication_zh": "成人抑郁",
        "clinical_scene_zh": "适合把学术证据真正转成临床路径、分层管理和治疗优先级时使用。",
        "key_techniques_en": "CBT; behavioral activation; IPT; short-term psychodynamic approaches; stepped care",
        "key_techniques_zh": "CBT、行为激活、IPT、短程动力学治疗、分层照护",
        "evidence_level": "High",
        "recommendation_level_zh": "核心指南",
        "abstract_summary_zh": "NICE 不是原始研究，但它把证据转成了临床决策路径。学习时，它最适合帮助你把‘知道有证据’变成‘知道何时该优先什么’。",
        "why_included_zh": "作为英美以外地区也常参考的主流循证指南，具有很强的实践转换价值。",
        "practical_takeaway_zh": "当你需要把研究转成实际方案排序时，先回到指南。",
        "can_be_used_as_core_evidence": "yes",
        "manual_authors": "National Institute for Health and Care Excellence",
        "manual_year": "2022",
        "manual_journal": "NICE Guideline",
        "manual_doi": "",
        "manual_pmid": "",
        "primary_url": "https://www.nice.org.uk/guidance/ng222",
    },
    {
        "citation_id": "guideline_apa_2019_depression",
        "query": {"type": "manual", "value": "https://www.apa.org/depression-guideline"},
        "folder": "02_guidelines",
        "subfolder": "depression",
        "title_en_manual": "Clinical Practice Guideline for the Treatment of Depression Across Three Age Cohorts",
        "title_zh": "跨三个年龄队列的抑郁治疗临床实践指南",
        "study_design_zh": "临床实践指南",
        "therapy_modality_en": "Guideline-level multimodal recommendations",
        "therapy_modality_zh": "指南级多模式治疗建议",
        "indication_en": "Depression across age cohorts",
        "indication_zh": "不同年龄层抑郁治疗",
        "clinical_scene_zh": "适合比较儿童青少年、成人和老年群体在抑郁治疗推荐上的差异。",
        "key_techniques_en": "Evidence-based psychotherapy selection across age groups",
        "key_techniques_zh": "分年龄层的循证心理治疗选择",
        "evidence_level": "High",
        "recommendation_level_zh": "核心指南",
        "abstract_summary_zh": "APA 指南更强调跨年龄层决策，适合和 NICE 对照阅读。它能帮助你避免把成人证据机械搬到其他年龄层。",
        "why_included_zh": "补足美国体系下的推荐逻辑与年龄维度。",
        "practical_takeaway_zh": "同一种抑郁，不同年龄段的优先干预重点不一定相同。",
        "can_be_used_as_core_evidence": "yes",
        "manual_authors": "American Psychological Association",
        "manual_year": "2019",
        "manual_journal": "APA Guideline",
        "manual_doi": "",
        "manual_pmid": "",
        "primary_url": "https://www.apa.org/depression-guideline",
    },
    {
        "citation_id": "support_ataglance_2024",
        "query": {"type": "doi", "value": "10.1176/appi.psychotherapy.20230004"},
        "folder": "03_supporting_overviews",
        "subfolder": "general_psychotherapy",
        "title_zh": "心理治疗速览：成人精神障碍的指南共识推荐心理治疗",
        "study_design_zh": "指南概览 / 导航文献",
        "therapy_modality_en": "General psychotherapy overview",
        "therapy_modality_zh": "心理治疗总览",
        "indication_en": "Adult psychiatric disorders",
        "indication_zh": "成人精神障碍总览",
        "clinical_scene_zh": "适合快速建立‘什么障碍通常先想到什么治疗’的直观地图。",
        "key_techniques_en": "Overview-level recommendations",
        "key_techniques_zh": "概览级建议，不是单项技术试验",
        "evidence_level": "Moderate",
        "recommendation_level_zh": "补充推荐",
        "abstract_summary_zh": "这篇文章的作用更像地图而不是终局证据。它适合在扩文献前快速定位方向。",
        "why_included_zh": "作为检索导航非常高效，但不应替代原始综述和指南。",
        "practical_takeaway_zh": "先用它找方向，再回到核心证据。",
        "can_be_used_as_core_evidence": "no",
    },
    {
        "citation_id": "theory_shedler_2010",
        "query": {"type": "pmid", "value": "20141265"},
        "folder": "04_theory_and_perspective",
        "subfolder": "psychodynamic",
        "title_zh": "心理动力学心理治疗的疗效",
        "study_design_zh": "理论综述 / 观点性综述",
        "therapy_modality_en": "Psychodynamic psychotherapy",
        "therapy_modality_zh": "心理动力学治疗",
        "indication_en": "Cross-diagnostic theory discussion",
        "indication_zh": "跨诊断理论讨论",
        "clinical_scene_zh": "适合在你需要理解动力学流派为何长期被误解、它到底在做什么时阅读。",
        "key_techniques_en": "Psychodynamic concepts overview",
        "key_techniques_zh": "动力学概念总览",
        "evidence_level": "Supplementary",
        "recommendation_level_zh": "补充理论",
        "abstract_summary_zh": "它不是近年的系统综述，但对于理解动力学治疗的自我辩护逻辑和公共误解非常有用。",
        "why_included_zh": "保留为理论入口，不参与核心证据排序。",
        "practical_takeaway_zh": "用来看懂动力学，不要拿它单独扛疗效证据。",
        "can_be_used_as_core_evidence": "no",
    },
    {
        "citation_id": "official_dbt_faq",
        "query": {"type": "manual", "value": "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/"},
        "folder": "05_official_explainers",
        "subfolder": "dbt",
        "title_en_manual": "Dialectical Behavior Therapy (DBT) FAQ",
        "title_zh": "辩证行为治疗（DBT）常见问题",
        "study_design_zh": "机构说明文",
        "therapy_modality_en": "DBT",
        "therapy_modality_zh": "辩证行为治疗",
        "indication_en": "Emotion dysregulation and self-harm related presentations",
        "indication_zh": "情绪失调、自伤与高风险冲动相关表现",
        "clinical_scene_zh": "适合你想快速搞清 DBT 四大技能模块、治疗构成和训练方式时。",
        "key_techniques_en": "Mindfulness; distress tolerance; emotion regulation; interpersonal effectiveness",
        "key_techniques_zh": "正念、痛苦耐受、情绪调节、人际效能",
        "evidence_level": "Supplementary",
        "recommendation_level_zh": "机构说明",
        "abstract_summary_zh": "它不是学术综述，但非常适合解释 DBT 到底由什么构成，为什么它常常不是单次谈话式治疗。",
        "why_included_zh": "用于概念澄清和课程结构理解。",
        "practical_takeaway_zh": "把它当说明书，而不是当疗效证据。",
        "can_be_used_as_core_evidence": "no",
        "manual_authors": "Behavioral Tech",
        "manual_year": "n.d.",
        "manual_journal": "Official organization resource",
        "manual_doi": "",
        "manual_pmid": "",
        "primary_url": "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/",
    },
]


JOURNAL_METRICS = {
    "World Psychiatry": {
        "publisher": "Wiley-Blackwell",
        "quartile": "Q1",
        "sjr_2025": "18.419",
        "h_index_2025": "153",
        "overall_rank_2025": "19",
        "impact_score_2024_2025": "13.01",
        "scope": "Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/6200180159",
    },
    "JAMA Psychiatry": {
        "publisher": "American Medical Association",
        "quartile": "Q1",
        "sjr_2025": "5.755",
        "h_index_2025": "417",
        "overall_rank_2025": "228",
        "impact_score_2024_2025": "9.08",
        "scope": "Medicine (miscellaneous) (Q1); Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/21100228547",
    },
    "American Journal of Psychiatry": {
        "publisher": "American Psychiatric Association",
        "quartile": "Q1",
        "sjr_2025": "5.27",
        "h_index_2025": "405",
        "overall_rank_2025": "271",
        "impact_score_2024_2025": "6.67",
        "scope": "Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/17664",
    },
    "Clinical Psychology Review": {
        "publisher": "Elsevier Inc.",
        "quartile": "Q1",
        "sjr_2025": "6.617",
        "h_index_2025": "269",
        "overall_rank_2025": "180",
        "impact_score_2024_2025": "13.66",
        "scope": "Clinical Psychology (Q1); Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/12854",
    },
    "The Lancet Psychiatry": {
        "publisher": "Elsevier Ltd",
        "quartile": "Q1",
        "sjr_2025": "7.458",
        "h_index_2025": "160",
        "overall_rank_2025": "145",
        "impact_score_2024_2025": "7.51",
        "scope": "Biological Psychiatry (Q1); Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/21100356804",
    },
    "Depression and Anxiety": {
        "publisher": "John Wiley and Sons Inc",
        "quartile": "Q1",
        "sjr_2025": "2.007",
        "h_index_2025": "168",
        "overall_rank_2025": "1423",
        "impact_score_2024_2025": "3.64",
        "scope": "Clinical Psychology (Q1); Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/13487",
    },
    "Journal of Affective Disorders": {
        "publisher": "Elsevier B.V.",
        "quartile": "Q1",
        "sjr_2025": "2.121",
        "h_index_2025": "245",
        "overall_rank_2025": "1289",
        "impact_score_2024_2025": "5.42",
        "scope": "Clinical Psychology (Q1); Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/16245",
    },
    "Comprehensive Psychiatry": {
        "publisher": "W.B. Saunders",
        "quartile": "Q1",
        "sjr_2025": "1.718",
        "h_index_2025": "128",
        "overall_rank_2025": "1868",
        "impact_score_2024_2025": "5.30",
        "scope": "Clinical Psychology (Q1); Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/14921",
    },
    "International Journal of Eating Disorders": {
        "publisher": "John Wiley and Sons Inc",
        "quartile": "Q1",
        "sjr_2025": "1.703",
        "h_index_2025": "163",
        "overall_rank_2025": "1907",
        "impact_score_2024_2025": "4.35",
        "scope": "Psychiatry and Mental Health (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/12675",
    },
    "Journal of Psychiatric and Mental Health Nursing": {
        "publisher": "Wiley-Blackwell Publishing Ltd",
        "quartile": "Q2",
        "sjr_2025": "1.123",
        "h_index_2025": "78",
        "overall_rank_2025": "3987",
        "impact_score_2024_2025": "3.68",
        "scope": "Psychiatry and Mental Health (Q2)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/16796",
    },
    "American Journal of Psychotherapy": {
        "publisher": "American Psychiatric Association",
        "quartile": "Q2",
        "sjr_2025": "0.834",
        "h_index_2025": "58",
        "overall_rank_2025": "6371",
        "impact_score_2024_2025": "1.65",
        "scope": "Clinical Psychology (Q2); Medicine (miscellaneous) (Q2)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/17666",
    },
    "American Psychologist": {
        "publisher": "American Psychological Association",
        "quartile": "Q1",
        "sjr_2025": "3.2",
        "h_index_2025": "283",
        "overall_rank_2025": "637",
        "impact_score_2024_2025": "5.35",
        "scope": "Medicine (miscellaneous) (Q1); Psychology (miscellaneous) (Q1)",
        "metrics_source": "Resurchify / SCImago snapshot",
        "metrics_url": "https://www.resurchify.com/impact/details/29492",
    },
    "NICE Guideline": {
        "publisher": "National Institute for Health and Care Excellence",
        "quartile": "",
        "sjr_2025": "",
        "h_index_2025": "",
        "overall_rank_2025": "",
        "impact_score_2024_2025": "",
        "scope": "Clinical guideline",
        "metrics_source": "Institutional guideline",
        "metrics_url": "https://www.nice.org.uk/guidance/ng222",
    },
    "APA Guideline": {
        "publisher": "American Psychological Association",
        "quartile": "",
        "sjr_2025": "",
        "h_index_2025": "",
        "overall_rank_2025": "",
        "impact_score_2024_2025": "",
        "scope": "Clinical guideline",
        "metrics_source": "Institutional guideline",
        "metrics_url": "https://www.apa.org/depression-guideline",
    },
    "Official organization resource": {
        "publisher": "Behavioral Tech",
        "quartile": "",
        "sjr_2025": "",
        "h_index_2025": "",
        "overall_rank_2025": "",
        "impact_score_2024_2025": "",
        "scope": "Official explainer",
        "metrics_source": "Institutional explainer",
        "metrics_url": "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/",
    },
}


def ensure_dirs() -> None:
    for item in SOURCE_DEFS:
        (ROOT / item["folder"] / item["subfolder"]).mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    OA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "CodexAgent/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_epmc_record(query_type: str, query_value: str) -> dict:
    if query_type == "pmid":
        query = f"EXT_ID:{query_value} AND SRC:MED"
    elif query_type == "doi":
        query = f'DOI:"{query_value}"'
    else:
        return {}
    url = (
        "https://www.ebi.ac.uk/europepmc/webservices/rest/search?"
        f"query={urllib.parse.quote(query)}&resultType=core&format=json"
    )
    data = fetch_json(url)
    results = data.get("resultList", {}).get("result", [])
    if not results:
        return {}
    return results[0]


def choose_free_fulltext(record: dict) -> tuple[str, list[str]]:
    urls = []
    for item in record.get("fullTextUrlList", {}).get("fullTextUrl", []) or []:
        url = item.get("url", "")
        availability = item.get("availabilityCode", "")
        if url:
            urls.append((availability, url))
    free = [u for availability, u in urls if availability == "F"]
    all_urls = [u for _, u in urls]
    if record.get("pmcid"):
        pmc_article = f"https://pmc.ncbi.nlm.nih.gov/articles/{record['pmcid']}/"
        if pmc_article not in all_urls:
            all_urls.append(pmc_article)
        if not free:
            free.append(pmc_article)
    best = free[0] if free else (all_urls[0] if all_urls else "")
    return best, all_urls


def download_pdf_from_urls(record: dict, stem: str, all_urls: list[str]) -> str:
    candidate_urls = []
    for url in all_urls:
        if any(token in url.lower() for token in ["pdf", "articlepdf", "render"]):
            candidate_urls.append(url)
    pmcid = record.get("pmcid", "")
    if pmcid:
        candidate_urls.append(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/pdf/?download=1")
        candidate_urls.append(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/pdf/")
        candidate_urls.append(f"https://europepmc.org/articles/{pmcid}?pdf=render")
    target = PDF_DIR / f"{stem}.pdf"
    for pdf_url in candidate_urls:
        try:
            req = urllib.request.Request(pdf_url, headers={"User-Agent": "CodexAgent/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
            if data.startswith(b"%PDF"):
                target.write_bytes(data)
                return str(target)
        except Exception:
            continue
    return ""


def write_url_shortcut(path: Path, url: str) -> None:
    path.write_text(f"[InternetShortcut]\nURL={url}\n", encoding="ascii")


def journal_metrics_for(name: str) -> dict:
    if name in JOURNAL_METRICS:
        return JOURNAL_METRICS[name]

    normalized = (name or "").strip().lower()

    alias_map = {
        "clin psychol rev": "Clinical Psychology Review",
        "clinical psychology review": "Clinical Psychology Review",
        "jama psychiatry": "JAMA Psychiatry",
        "am j psychiatry": "American Journal of Psychiatry",
        "american journal of psychiatry": "American Journal of Psychiatry",
        "world psychiatry": "World Psychiatry",
        "depress anxiety": "Depression and Anxiety",
        "depression and anxiety": "Depression and Anxiety",
        "j affect disord": "Journal of Affective Disorders",
        "journal of affective disorders": "Journal of Affective Disorders",
        "compr psychiatry": "Comprehensive Psychiatry",
        "comprehensive psychiatry": "Comprehensive Psychiatry",
        "int j eat disord": "International Journal of Eating Disorders",
        "international journal of eating disorders": "International Journal of Eating Disorders",
        "j psychiatr ment health nurs": "Journal of Psychiatric and Mental Health Nursing",
        "journal of psychiatric and mental health nursing": "Journal of Psychiatric and Mental Health Nursing",
        "am psychol": "American Psychologist",
        "american psychologist": "American Psychologist",
        "american journal of psychotherapy": "American Journal of Psychotherapy",
        "lancet psychiatry": "The Lancet Psychiatry",
        "the lancet psychiatry": "The Lancet Psychiatry",
        "the lancet. psychiatry": "The Lancet Psychiatry",
    }

    for alias, canonical in alias_map.items():
        if alias in normalized:
            return JOURNAL_METRICS.get(canonical, {})

    return {}


def record_from_source(src: dict) -> dict:
    query = src["query"]
    epmc = {} if query["type"] == "manual" else fetch_epmc_record(query["type"], query["value"])

    title_en = src.get("title_en_manual") or clean_text(epmc.get("title", ""))
    title_zh = src["title_zh"]
    authors = src.get("manual_authors") or clean_text(epmc.get("authorString", ""))
    year = src.get("manual_year") or epmc.get("pubYear", "")
    journal = src.get("manual_journal") or clean_text(
        (epmc.get("journalInfo", {}).get("journal", {}) or {}).get("title", "") or epmc.get("journalTitle", "")
    )
    doi = src.get("manual_doi") or epmc.get("doi", "")
    pmid = src.get("manual_pmid") or epmc.get("pmid", "")
    pmcid = epmc.get("pmcid", "")
    abstract_en = clean_text(epmc.get("abstractText", ""))
    best_fulltext, all_fulltexts = choose_free_fulltext(epmc)
    primary_url = src.get("primary_url") or (f"https://doi.org/{doi}" if doi else best_fulltext)
    metrics = journal_metrics_for(journal)

    if epmc:
        if epmc.get("inPMC") == "Y":
            oa_status = "Free in PMC"
        elif best_fulltext:
            oa_status = "Free full text detected"
        elif epmc.get("isOpenAccess") == "Y":
            oa_status = "Open access detected"
        else:
            oa_status = "No free full text detected"
    else:
        oa_status = "Manual / not queried"

    stem = f"{year}_{src['citation_id']}"
    local_pdf = download_pdf_from_urls(epmc, stem, all_fulltexts) if epmc else ""

    return {
        "citation_id": src["citation_id"],
        "folder": src["folder"],
        "subfolder": src["subfolder"],
        "title_en": title_en,
        "title_zh": title_zh,
        "authors": authors,
        "year": year,
        "journal": journal,
        "study_design_zh": src["study_design_zh"],
        "therapy_modality_en": src["therapy_modality_en"],
        "therapy_modality_zh": src["therapy_modality_zh"],
        "indication_en": src["indication_en"],
        "indication_zh": src["indication_zh"],
        "clinical_scene_zh": src["clinical_scene_zh"],
        "key_techniques_en": src["key_techniques_en"],
        "key_techniques_zh": src["key_techniques_zh"],
        "evidence_level": src["evidence_level"],
        "recommendation_level_zh": src["recommendation_level_zh"],
        "pmid": pmid,
        "pmcid": pmcid,
        "doi": doi,
        "citation_count_epmc": epmc.get("citedByCount", ""),
        "citation_count_source": "Europe PMC citedByCount" if epmc else "",
        "citation_count_snapshot_date": SNAPSHOT_DATE if epmc else "",
        "is_open_access": epmc.get("isOpenAccess", ""),
        "in_pmc": epmc.get("inPMC", ""),
        "has_pdf": epmc.get("hasPDF", ""),
        "auth_manuscript": epmc.get("authMan", ""),
        "best_free_fulltext_url": best_fulltext,
        "all_fulltext_urls": " | ".join(all_fulltexts),
        "primary_url": primary_url,
        "local_pmc_pdf": local_pdf,
        "abstract_en": abstract_en,
        "abstract_summary_zh": src["abstract_summary_zh"],
        "why_included_zh": src["why_included_zh"],
        "practical_takeaway_zh": src["practical_takeaway_zh"],
        "can_be_used_as_core_evidence": src["can_be_used_as_core_evidence"],
        "journal_publisher": metrics.get("publisher", ""),
        "journal_best_quartile": metrics.get("quartile", ""),
        "journal_sjr_2025": metrics.get("sjr_2025", ""),
        "journal_h_index_2025": metrics.get("h_index_2025", ""),
        "journal_rank_2025": metrics.get("overall_rank_2025", ""),
        "journal_impact_score_2024_2025": metrics.get("impact_score_2024_2025", ""),
        "journal_scope": metrics.get("scope", ""),
        "journal_metrics_source": metrics.get("metrics_source", ""),
        "journal_metrics_url": metrics.get("metrics_url", ""),
    }


def write_card(record: dict) -> None:
    target_dir = ROOT / record["folder"] / record["subfolder"]
    file_stem = f"{record['year']}_{record['citation_id']}"
    note_path = target_dir / f"{file_stem}.md"
    primary_url_path = target_dir / f"{file_stem}.url"
    if record["primary_url"]:
        write_url_shortcut(primary_url_path, record["primary_url"])
    if record["best_free_fulltext_url"]:
        write_url_shortcut(OA_DIR / f"{file_stem}_fulltext.url", record["best_free_fulltext_url"])

    note = f"""# {record['title_en']}

## 中文标题

{record['title_zh']}

## Basic Citation

- citation_id: {record['citation_id']}
- authors: {record['authors']}
- year: {record['year']}
- journal: {record['journal']}
- study_design_zh: {record['study_design_zh']}
- doi: {record['doi']}
- pmid: {record['pmid']}
- pmcid: {record['pmcid']}

## 流派与适应症

- therapy_modality_en: {record['therapy_modality_en']}
- therapy_modality_zh: {record['therapy_modality_zh']}
- indication_en: {record['indication_en']}
- indication_zh: {record['indication_zh']}
- recommendation_level_zh: {record['recommendation_level_zh']}
- can_be_used_as_core_evidence: {record['can_be_used_as_core_evidence']}

## 生活中的典型场景

{record['clinical_scene_zh']}

## 核心技术 / 干预手段

- EN: {record['key_techniques_en']}
- 中文: {record['key_techniques_zh']}

## Abstract (English)

{record['abstract_en'] or 'No abstract captured.'}

## 摘要总结（中文）

{record['abstract_summary_zh']}

## 为什么纳入

{record['why_included_zh']}

## 实操启发

{record['practical_takeaway_zh']}

## 开放获取与全文

- primary_url: {record['primary_url']}
- best_free_fulltext_url: {record['best_free_fulltext_url']}
- all_fulltext_urls: {record['all_fulltext_urls']}
- local_pmc_pdf: {record['local_pmc_pdf']}
- is_open_access: {record['is_open_access']}
- in_pmc: {record['in_pmc']}
- has_pdf: {record['has_pdf']}
- auth_manuscript: {record['auth_manuscript']}

## 引用量与期刊质量信号

- article_citation_count: {record['citation_count_epmc']}
- citation_count_source: {record['citation_count_source']}
- citation_snapshot_date: {record['citation_count_snapshot_date']}
- journal_publisher: {record['journal_publisher']}
- journal_best_quartile: {record['journal_best_quartile']}
- journal_sjr_2025: {record['journal_sjr_2025']}
- journal_h_index_2025: {record['journal_h_index_2025']}
- journal_rank_2025: {record['journal_rank_2025']}
- journal_impact_score_2024_2025: {record['journal_impact_score_2024_2025']}
- journal_scope: {record['journal_scope']}
- journal_metrics_source: {record['journal_metrics_source']}
- journal_metrics_url: {record['journal_metrics_url']}
"""
    note_path.write_text(note, encoding="utf-8")


def write_index(records: list[dict]) -> None:
    csv_path = ROOT / "reference_index_bilingual.csv"
    fields = [
        "citation_id",
        "folder",
        "subfolder",
        "title_en",
        "title_zh",
        "authors",
        "year",
        "journal",
        "study_design_zh",
        "therapy_modality_en",
        "therapy_modality_zh",
        "indication_en",
        "indication_zh",
        "clinical_scene_zh",
        "key_techniques_en",
        "key_techniques_zh",
        "evidence_level",
        "recommendation_level_zh",
        "citation_count_epmc",
        "citation_count_source",
        "citation_count_snapshot_date",
        "journal_publisher",
        "journal_best_quartile",
        "journal_sjr_2025",
        "journal_h_index_2025",
        "journal_rank_2025",
        "journal_impact_score_2024_2025",
        "journal_scope",
        "journal_metrics_source",
        "journal_metrics_url",
        "pmid",
        "pmcid",
        "doi",
        "is_open_access",
        "in_pmc",
        "has_pdf",
        "auth_manuscript",
        "best_free_fulltext_url",
        "all_fulltext_urls",
        "primary_url",
        "local_pmc_pdf",
        "abstract_en",
        "abstract_summary_zh",
        "why_included_zh",
        "practical_takeaway_zh",
        "can_be_used_as_core_evidence",
    ]
    with csv_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in records:
            writer.writerow({k: row.get(k, "") for k in fields})

    md_path = ROOT / "reference_table_bilingual.md"
    lines = [
        "# Bilingual Reference Table",
        "",
        f"Snapshot date: {SNAPSHOT_DATE}",
        "",
        "| ID | 流派 | 适应症 | 证据类型 | 引用量 | OA | Q/Rank | 核心结论 |",
        "| --- | --- | --- | --- | ---: | --- | --- | --- |",
    ]
    for r in records:
        qrank = f"{r['journal_best_quartile']} / {r['journal_rank_2025']}" if r["journal_best_quartile"] or r["journal_rank_2025"] else "-"
        lines.append(
            f"| {r['citation_id']} | {r['therapy_modality_zh']} | {r['indication_zh']} | {r['study_design_zh']} | {r['citation_count_epmc'] or '-'} | {r['is_open_access'] or '-'} | {qrank} | {r['abstract_summary_zh']} |"
        )
    md_path.write_text("\n".join(lines), encoding="utf-8")

    oa_csv = ROOT / "open_access_index.csv"
    oa_fields = [
        "citation_id",
        "title_en",
        "pmcid",
        "is_open_access",
        "in_pmc",
        "has_pdf",
        "auth_manuscript",
        "best_free_fulltext_url",
        "all_fulltext_urls",
        "local_pmc_pdf",
    ]
    with oa_csv.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=oa_fields)
        writer.writeheader()
        for row in records:
            writer.writerow({k: row.get(k, "") for k in oa_fields})

    legacy_csv = ROOT / "reference_index.csv"
    with legacy_csv.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in records:
            writer.writerow({k: row.get(k, "") for k in fields})


def write_bibtex(records: list[dict]) -> None:
    entries = []
    for r in records:
        entry_type = "article" if r["doi"] or "journal" in r["journal"].lower() else "misc"
        title = r["title_en"].replace("{", "").replace("}", "")
        authors = r["authors"].replace("{", "").replace("}", "")
        journal = r["journal"].replace("{", "").replace("}", "")
        url = r["primary_url"] or r["best_free_fulltext_url"]
        lines = [
            f"@{entry_type}{{{r['citation_id']},",
            f"  title = {{{title}}},",
            f"  author = {{{authors}}},",
            f"  year = {{{r['year']}}},",
        ]
        if journal:
            lines.append(f"  journal = {{{journal}}},")
        if r["doi"]:
            lines.append(f"  doi = {{{r['doi']}}},")
        if url:
            lines.append(f"  url = {{{url}}},")
        lines.append("}")
        entries.append("\n".join(lines))
    (ROOT / "citations.bib").write_text("\n\n".join(entries) + "\n", encoding="utf-8")


def write_readme(records: list[dict]) -> None:
    total = len(records)
    core = sum(1 for r in records if r["can_be_used_as_core_evidence"] == "yes")
    pmc = sum(1 for r in records if r["in_pmc"] == "Y")
    oa = sum(1 for r in records if r["best_free_fulltext_url"])
    local_pdfs = sum(1 for r in records if r["local_pmc_pdf"])
    text = f"""# Reference Archive v2

This archive was expanded on {SNAPSHOT_DATE}.

## What changed

- Added more indication-specific sources across anxiety, PTSD, OCD, BPD, perinatal mental health, schizophrenia relapse prevention, and adolescent anorexia.
- Converted the archive into a bilingual format with English titles plus Chinese interpretation fields.
- Added abstract summaries, practical scene descriptions, technique labels, citation counts, and journal quality signals.
- Added an open-access index and attempted PMC PDF downloads where available.

## Main files

- `reference_index_bilingual.csv`: full bilingual master table.
- `reference_table_bilingual.md`: quick human-readable table.
- `open_access_index.csv`: open-access / PMC / PDF access routes.
- `_downloads_pmc_pdfs/`: locally downloaded PMC PDFs when available.

## Evidence note

- Total records: {total}
- Core evidence records: {core}
- Records with PMC presence: {pmc}
- Records with a free-full-text route detected: {oa}
- Local PDFs successfully downloaded: {local_pdfs}

## Citation count note

Article-level citation counts were captured from Europe PMC when available and should be treated as a dated snapshot, not a permanently fixed number.

## Journal metrics note

Journal metrics were added mainly from Resurchify pages that summarize Scopus/SCImago-based indicators such as best quartile, SJR, h-index, overall rank, and impact score. These are useful quality signals, but they are journal-level signals rather than direct proof of an individual article's quality.
"""
    (ROOT / "README_v2.md").write_text(text, encoding="utf-8")


def main() -> None:
    ensure_dirs()
    records = [record_from_source(src) for src in SOURCE_DEFS]
    for record in records:
        write_card(record)
    write_index(records)
    write_bibtex(records)
    write_readme(records)


if __name__ == "__main__":
    main()
