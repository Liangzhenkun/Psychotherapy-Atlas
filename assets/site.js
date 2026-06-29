const siteContent = {
  zh: {
    pageTitle: "Psychotherapy Atlas",
    htmlLang: "zh-CN",
    hero: {
      kicker: "Research Atlas / Narrative Reference",
      title: "心理治疗地图",
      subtitle: "把综述文献、治疗技术、适应症、生活表现与创作转译放进同一张地图里，方便系统学习，也方便后续做叙事、角色和作品集。",
      meta: ["更新日期：2026-06-30", "主题：流派、技术、适应症与叙事转译", "形式：中英可切换静态站点"],
      links: [
        { label: "中文研究包 Markdown", href: "psychotherapy_research_pack.md" },
        { label: "English Research Pack", href: "psychotherapy_research_pack_en.md" },
        { label: "文献归档表", href: "reference_archive/reference_table_bilingual.md" }
      ]
    },
    toc: {
      title: "目录",
      items: [
        ["overview", "项目结构"],
        ["core", "核心综述"],
        ["map", "流派-技术-适应症"],
        ["life", "生活表现"],
        ["search", "检索策略"],
        ["craft", "创作转译"],
        ["works", "艺术作品"],
        ["ideas", "故事钩子"],
        ["archive", "文献归档"],
        ["sources", "来源"]
      ]
    },
    overview: {
      title: "项目结构",
      lede: "这套材料按“研究地图”的逻辑组织。它既能做学习入口，也能做后续扩展的底盘。",
      layers: [
        ["证据底盘", "核心系统综述、元分析、网络元分析与指南。"],
        ["临床映射", "把流派、技术、适应症和推荐强度放进同一张表。"],
        ["识别能力", "把临床语言翻译成日常生活中的模式识别。"],
        ["创作转译", "把治疗视角转成角色、关系、冲突与主题。"] 
      ],
      note: "循证推荐等级是基于近年综述与 NICE、APA 指南的综合工作判断，不等同于某一份单独指南里的官方 GRADE。"
    },
    core: {
      title: "核心综述",
      lede: "先读这些文献，足够搭起一张稳定的入门到中高阶框架。",
      cards: [
        {
          tag: "Umbrella Review",
          title: "成人精神障碍中心理治疗与药物治疗的疗效",
          body: "跨流派总览。CBT 证据最广；IPT 在抑郁领域很强；动力学治疗在抑郁、焦虑和人格相关问题上有稳定支持；系统干预在特定人群里优势明确。",
          links: [{ label: "DOI", href: "https://doi.org/10.1017/S0033291721002965" }]
        },
        {
          tag: "Meta-Analyses",
          title: "CBT 在精神障碍治疗中的统一元分析",
          body: "适合用来建立 CBT 总图。认知重构、行为激活、暴露、行为实验和问题解决是最常见的核心技术。",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/40238104/" }]
        },
        {
          tag: "Comprehensive Meta-Analysis",
          title: "IPT 用于精神健康问题的综合元分析",
          body: "IPT 的重点是关系事件。对抑郁尤其是成人与围产期抑郁证据较强，适合丧亲、分手、角色变化、照护压力等情境。",
          links: [{ label: "VU Research", href: "https://research.vu.nl/en/publications/interpersonal-psychotherapy-for-mental-health-problems-a-comprehe" }]
        },
        {
          tag: "Meta-Analysis",
          title: "短程动力学治疗用于抑郁的疗效与调节因素",
          body: "适合反复陷入同类关系脚本、情感表达受阻、防御明显的人群。重点不在单一技术，而在模式识别与修通。",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/36958077/" }]
        },
        {
          tag: "Network Meta-Analysis",
          title: "家庭干预用于精神分裂症复发预防",
          body: "系统治疗在这一适应症上有明确强项。家庭心理教育、沟通训练与复发预警管理能实质降低复发风险。",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/35462002/" }]
        },
        {
          tag: "Optional Reading",
          title: "抑郁治疗的横向比较补充",
          body: "适合理解为什么不同流派在抑郁上的总疗效接近，但适配人群、技术路径和治疗体验仍然明显不同。",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/34135080/" }]
        }
      ]
    },
    map: {
      title: "流派-技术-适应症映射",
      lede: "把流派、实操技术和最常见的高价值适应症放进同一张工作表里。",
      headers: ["治疗流派", "核心技术", "最佳适应症", "推荐等级"],
      rows: [
        ["认知行为取向（CBT / DBT）", "认知重构、行为激活、暴露、行为实验、链式分析、情绪调节、痛苦耐受、反向行动", "抑郁、GAD、惊恐、社交焦虑、OCD、PTSD；DBT 适合边缘型人格障碍伴自伤/自杀风险", "强烈推荐"],
        ["心理动力学取向（PDT / STDP）", "澄清、对抗、解释、防御分析、情感聚焦、关系主题识别、移情/反移情工作", "抑郁、长期关系困扰、人格功能问题、反复重演式人际模式、部分心身问题", "中度推荐"],
        ["人际关系取向（IPT）", "角色转变工作、哀伤工作、人际争端分析、沟通分析、社会支持重建、情感命名", "成人抑郁、围产期/产后抑郁、与关系事件紧密相关的情绪障碍", "强烈推荐"],
        ["系统家庭治疗取向", "家谱图、循环提问、联盟与界限调整、现场互动演练、家庭心理教育、沟通训练、问题解决", "精神分裂症复发预防、青少年厌食症、外化问题、家庭冲突高度卷入个案", "中度推荐"]
      ],
      note: "一个实用的记法是：CBT 改回路，动力学改脚本，IPT 改关系失衡后的适应，系统治疗改互动机器。"
    },
    life: {
      title: "生活中的表现",
      lede: "真正能把知识讲明白，关键在于你能不能把文献语言翻译成可识别的现实场景。",
      cards: [
        ["CBT / DBT", "常见于灾难化预测、回避、自我否定、反复确认，或情绪海啸后出现冲动、自伤、剧烈羞耻的个体。"],
        ["PDT / STDP", "常见于总爱上同一种人、关键时刻退缩或攻击、愤怒说不出口、亲密关系里不断重演旧模式的人。"],
        ["IPT", "常见于迁居、毕业、离婚、婚育、丧亲、照护压力后明显恶化的情绪问题。"],
        ["Systemic / Family", "常见于“问题孩子”承担全家裂缝、一个成员改善另一个成员就失控、复发与高批评高卷入气氛同步上升的家庭。"]
      ]
    },
    search: {
      title: "高级检索策略",
      lede: "这些 Google Scholar 检索式适合继续扩充文献库。",
      items: [
        ["总体循证图谱", "(\"psychotherapy\" OR \"psychological treatment\") AND (\"umbrella review\" OR \"meta-analysis\" OR \"network meta-analysis\") AND (\"mental disorders\" OR depression OR anxiety) AND (indications OR moderators OR predictors)"],
        ["CBT / DBT", "(\"cognitive behavioral therapy\" OR CBT OR \"dialectical behavior therapy\" OR DBT) AND (\"cognitive restructuring\" OR exposure OR \"behavioral activation\" OR \"emotion regulation\") AND (depression OR anxiety OR OCD OR PTSD OR \"borderline personality disorder\") AND (\"systematic review\" OR \"meta-analysis\")"],
        ["心理动力学治疗", "(\"psychodynamic therapy\" OR \"short-term psychodynamic psychotherapy\" OR STPP OR PDT) AND (transference OR interpretation OR defense OR \"affect focus\") AND (depression OR anxiety OR personality) AND (\"meta-analysis\" OR \"systematic review\")"],
        ["IPT", "(\"interpersonal psychotherapy\" OR IPT) AND (\"role transition\" OR grief OR \"interpersonal disputes\" OR \"social support\") AND (depression OR perinatal OR postpartum OR anxiety OR \"eating disorder\") AND (\"meta-analysis\" OR \"systematic review\")"],
        ["系统 / 家庭治疗", "(\"family therapy\" OR \"systemic therapy\" OR \"family intervention\" OR \"family psychoeducation\") AND (schizophrenia OR \"eating disorders\" OR adolescents OR OCD OR substance) AND (\"systematic review\" OR \"meta-analysis\" OR \"network meta-analysis\")"]
      ]
    },
    craft: {
      title: "创作转译",
      lede: "把治疗流派当作人物命运的分析镜头，比把它们写成咨询室对白更有用。",
      headers: ["流派", "叙事镜头", "适合塑造的冲突"],
      rows: [
        ["CBT / DBT", "错误预测如何一步步变成现实；情绪如何裹挟行为", "羞耻、恐惧、回避、冲动、自毁、创伤后回缩"],
        ["动力学", "过去未解冲突如何伪装成当下选择", "重复性命运、依恋、欲望与防御、亲密失败"],
        ["IPT", "关系事件如何改变一个人的自我状态", "丧失、迁移、婚育、代际角色转换、社会支持断裂"],
        ["系统家庭", "症状如何在群体中承担维稳功能", "家族秘密、替罪羊、联盟、照护耗竭、复发循环"]
      ],
      themesTitle: "可反复使用的临床母题",
      themes: [
        "替罪羊角色：一个人替整个家庭承担无法言说的冲突。",
        "重复性恋爱：主角总在不同阶段爱上“同一种人”。",
        "症状作为忠诚：角色不愿痊愈，因为痊愈意味着背叛旧关系。",
        "角色转变危机：毕业、继承、婚育、移民、失业后人格结构失衡。",
        "高情绪表达家庭：所谓“为你好”恰恰成为复发触发器。"
      ]
    },
    works: {
      title: "艺术作品参考",
      lede: "这些作品不一定直接讲心理治疗，但很适合用来观察症状、关系与命运结构。",
      items: [
        ["Film", "Good Will Hunting", "依恋创伤、羞耻防御、矫正性关系经验。", "https://en.wikipedia.org/wiki/Good_Will_Hunting"],
        ["Film", "Ordinary People", "很适合从 IPT 与家庭系统视角看哀伤、沉默和症状外显。", "https://en.wikipedia.org/wiki/Ordinary_People"],
        ["Series", "The Sopranos", "适合观察移情、防御、治疗关系中的操控与权力。", "https://www.hbo.com/the-sopranos"],
        ["Game", "Disco Elysium", "把内在多声部、自我叙事与行为选择回路做成机制的高质量参考。", "https://discoelysium.com/"],
        ["Game", "Hellblade: Senua's Sacrifice", "适合观察精神病性体验如何被艺术化地感知化。", "https://www.hellblade.com/"],
        ["Novel", "The Bell Jar", "适合书写抑郁、身份窒息和社会角色压力。", "https://en.wikipedia.org/wiki/The_Bell_Jar"]
      ]
    },
    ideas: {
      title: "原创故事钩子",
      lede: "下面这些设定已经可以直接转成世界观草图、角色弧线或互动机制。",
      cards: [
        ["Systemic", "症状是家族的保险丝", "一名反复惊恐与失语的女孩，实际上在替整个家族承担祖辈秘密；一旦她好起来，隐藏联盟就会暴露。"],
        ["Psychodynamic", "主角爱上的永远是同一个人", "不同城市、不同年龄、不同职业阶段，她总爱上不可获得的人，真正被重复的是一段早年的关系脚本。"],
        ["CBT", "自动化思维篡改世界 UI", "灾难化思维会实时扭曲地图、NPC 表情和任务文本；玩家必须通过行为实验和暴露来校准现实。"],
        ["IPT", "失去被需要的位置之后", "照护重病母亲多年的青年在母亲去世后迅速抑郁，核心不是单一丧亲，而是社会角色塌陷后的重返人群。"]
      ]
    },
    archive: {
      title: "文献归档",
      lede: "仓库里保留了可审查的文献归档，包含中英文条目、摘要总结、开放获取链接、部分全文 PDF、引用量和期刊评级信息。",
      items: [
        ["双语总表", "快速查看文献标题、适应症、治疗技术、引用量、期刊分区与摘要总结。", "reference_archive/reference_table_bilingual.md"],
        ["双语索引 CSV", "适合导入表格软件做筛选、排序和二次整理。", "reference_archive/reference_index_bilingual.csv"],
        ["开放获取索引", "集中查看 PMC、作者手稿版、PDF 和开放链接。", "reference_archive/open_access_index.csv"],
        ["参考文献 BibTeX", "便于后续写作或转入 Zotero / JabRef。", "reference_archive/citations.bib"],
        ["归档说明", "说明目录结构、命名逻辑与可用资源范围。", "reference_archive/README_v2.md"],
        ["审计说明", "记录归档构建与质量控制说明。", "reference_archive/AGENT_AUDIT_SUMMARY.md"]
      ]
    },
    sources: {
      title: "来源",
      lede: "页面只列主干来源；完整归档见文献目录。",
      coreTitle: "核心学术来源",
      extraTitle: "指南与补充",
      core: [
        ["Leichsenring et al. 2022", "https://doi.org/10.1017/S0033291721002965"],
        ["Cuijpers et al. 2025", "https://pubmed.ncbi.nlm.nih.gov/40238104/"],
        ["Cuijpers et al. 2016", "https://research.vu.nl/en/publications/interpersonal-psychotherapy-for-mental-health-problems-a-comprehe"],
        ["Wienicke et al. 2023", "https://pubmed.ncbi.nlm.nih.gov/36958077/"],
        ["Rodolico et al. 2022", "https://pubmed.ncbi.nlm.nih.gov/35462002/"],
        ["Cuijpers et al. 2021", "https://pubmed.ncbi.nlm.nih.gov/34135080/"]
      ],
      extra: [
        ["NICE NG222", "https://www.nice.org.uk/guidance/ng222"],
        ["APA Depression Guideline", "https://www.apa.org/depression-guideline"],
        ["Psychotherapies at a Glance", "https://psychiatryonline.org/doi/10.1176/appi.psychotherapy.20230035"],
        ["Shedler 2010", "https://pubmed.ncbi.nlm.nih.gov/20141265/"],
        ["Behavioral Tech DBT FAQ", "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/"]
      ]
    }
  },
  en: {
    pageTitle: "Psychotherapy Atlas",
    htmlLang: "en",
    hero: {
      kicker: "Research Atlas / Narrative Reference",
      title: "Psychotherapy Atlas",
      subtitle: "A bilingual map of review papers, therapeutic techniques, indications, everyday presentation patterns, and narrative translation for study, design, and portfolio work.",
      meta: ["Updated: June 30, 2026", "Focus: approaches, techniques, indications, narrative translation", "Format: bilingual static site with language switch"],
      links: [
        { label: "Chinese Research Pack", href: "psychotherapy_research_pack.md" },
        { label: "English Research Pack", href: "psychotherapy_research_pack_en.md" },
        { label: "Bilingual Reference Table", href: "reference_archive/reference_table_bilingual.md" }
      ]
    },
    toc: {
      title: "Contents",
      items: [
        ["overview", "Project Structure"],
        ["core", "Core Reviews"],
        ["map", "Approach-Technique-Indication Map"],
        ["life", "Everyday Presentation"],
        ["search", "Search Strategy"],
        ["craft", "Narrative Translation"],
        ["works", "Art References"],
        ["ideas", "Story Hooks"],
        ["archive", "Reference Archive"],
        ["sources", "Sources"]
      ]
    },
    overview: {
      title: "Project Structure",
      lede: "This project is organized as a working research atlas rather than a loose reading list.",
      layers: [
        ["Evidence Base", "Core systematic reviews, meta-analyses, network meta-analyses, and guidelines."],
        ["Clinical Map", "A working table linking approaches, techniques, indications, and recommendation strength."],
        ["Recognition Layer", "Translation from clinical language into recognizable real-life patterns."],
        ["Creative Translation", "A bridge from psychotherapy concepts to character, conflict, relationship, and theme."]
      ],
      note: "Recommendation levels here are a working synthesis based on recent reviews plus NICE and APA guidance, not a direct copy of any single guideline's official GRADE table."
    },
    core: {
      title: "Core Reviews",
      lede: "These papers are enough to build a solid foundation from entry level to intermediate-advanced understanding.",
      cards: [
        {
          tag: "Umbrella Review",
          title: "Psychotherapies and pharmacotherapies for adult mental disorders",
          body: "A cross-modality overview. CBT has the broadest evidence base; IPT is especially strong for depression; psychodynamic treatment has stable support in depression, anxiety, and personality-related problems; systemic work shows clear strengths in selected populations.",
          links: [{ label: "DOI", href: "https://doi.org/10.1017/S0033291721002965" }]
        },
        {
          tag: "Meta-Analyses",
          title: "Unified meta-analytic overview of CBT",
          body: "Useful as a map of CBT across disorders. Cognitive restructuring, behavioral activation, exposure, behavioral experiments, and problem solving are among its most portable techniques.",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/40238104/" }]
        },
        {
          tag: "Comprehensive Meta-Analysis",
          title: "Interpersonal Psychotherapy for Mental Health Problems",
          body: "IPT is especially useful when symptoms are tightly linked to relationship events, grief, role transition, interpersonal conflict, or social disconnection.",
          links: [{ label: "VU Research", href: "https://research.vu.nl/en/publications/interpersonal-psychotherapy-for-mental-health-problems-a-comprehe" }]
        },
        {
          tag: "Meta-Analysis",
          title: "Short-term psychodynamic psychotherapy for depression",
          body: "Especially relevant for people who repeat similar relationship scripts, struggle with emotional expression, or rely heavily on defensive organization.",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/36958077/" }]
        },
        {
          tag: "Network Meta-Analysis",
          title: "Family interventions for relapse prevention in schizophrenia",
          body: "A strong example of systemic treatment in a clear indication area. Family psychoeducation, communication training, and relapse planning can reduce relapse risk in meaningful ways.",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/35462002/" }]
        },
        {
          tag: "Optional Reading",
          title: "Cross-treatment comparison for depression",
          body: "Helpful for understanding why several therapies can show similar overall efficacy in depression while still feeling very different in technique, fit, and therapeutic experience.",
          links: [{ label: "PubMed", href: "https://pubmed.ncbi.nlm.nih.gov/34135080/" }]
        }
      ]
    },
    map: {
      title: "Approach-Technique-Indication Map",
      lede: "A compact working table that connects treatment families, hands-on methods, and high-value indications.",
      headers: ["Approach", "Core Techniques", "Best-Fit Indications", "Recommendation Level"],
      rows: [
        ["Cognitive-behavioral approaches (CBT / DBT)", "Cognitive restructuring, behavioral activation, exposure, behavioral experiments, chain analysis, emotion regulation, distress tolerance, opposite action", "Depression, GAD, panic, social anxiety, OCD, PTSD; DBT is especially useful for BPD with self-harm or suicide risk", "Strong"],
        ["Psychodynamic approaches (PDT / STDP)", "Clarification, confrontation, interpretation, defense analysis, affect focus, relationship-theme tracking, transference/countertransference work", "Depression, chronic relational difficulty, personality functioning problems, repetitive interpersonal patterns, some psychosomatic presentations", "Moderate"],
        ["Interpersonal approach (IPT)", "Role transition work, grief work, interpersonal dispute analysis, communication analysis, rebuilding support, affect naming", "Adult depression, perinatal/postpartum depression, mood problems strongly tied to relationship events", "Strong"],
        ["Systemic / family therapy", "Genograms, circular questioning, alliance and boundary work, in-session interaction practice, family psychoeducation, communication training, problem solving", "Schizophrenia relapse prevention, adolescent anorexia, externalizing problems, high-conflict family-involved cases", "Moderate"]
      ],
      note: "A simple memory aid: CBT changes loops, psychodynamic work changes scripts, IPT changes adaptation to relational imbalance, and systemic work changes the interaction machine."
    },
    life: {
      title: "Everyday Presentation",
      lede: "A useful test of understanding is whether you can translate the literature into recognizable everyday scenes.",
      cards: [
        ["CBT / DBT", "Common where catastrophic prediction, avoidance, self-negation, reassurance seeking, or emotion-driven impulsive behavior dominate the clinical picture."],
        ["PDT / STDP", "Common where people keep choosing the same kind of unavailable partner, shut down at key moments, or reenact old relational patterns without understanding why."],
        ["IPT", "Common where symptoms worsen after relocation, graduation, divorce, parenthood, bereavement, or caregiving strain."],
        ["Systemic / Family", "Common where one member carries the family symptom, improvement in one person destabilizes another, or relapse rises with criticism and over-involvement."]
      ]
    },
    search: {
      title: "Search Strategy",
      lede: "These Google Scholar strings are designed for expanding the literature base with precision.",
      items: [
        ["Overall evidence map", "(\"psychotherapy\" OR \"psychological treatment\") AND (\"umbrella review\" OR \"meta-analysis\" OR \"network meta-analysis\") AND (\"mental disorders\" OR depression OR anxiety) AND (indications OR moderators OR predictors)"],
        ["CBT / DBT", "(\"cognitive behavioral therapy\" OR CBT OR \"dialectical behavior therapy\" OR DBT) AND (\"cognitive restructuring\" OR exposure OR \"behavioral activation\" OR \"emotion regulation\") AND (depression OR anxiety OR OCD OR PTSD OR \"borderline personality disorder\") AND (\"systematic review\" OR \"meta-analysis\")"],
        ["Psychodynamic therapy", "(\"psychodynamic therapy\" OR \"short-term psychodynamic psychotherapy\" OR STPP OR PDT) AND (transference OR interpretation OR defense OR \"affect focus\") AND (depression OR anxiety OR personality) AND (\"meta-analysis\" OR \"systematic review\")"],
        ["IPT", "(\"interpersonal psychotherapy\" OR IPT) AND (\"role transition\" OR grief OR \"interpersonal disputes\" OR \"social support\") AND (depression OR perinatal OR postpartum OR anxiety OR \"eating disorder\") AND (\"meta-analysis\" OR \"systematic review\")"],
        ["Systemic / family therapy", "(\"family therapy\" OR \"systemic therapy\" OR \"family intervention\" OR \"family psychoeducation\") AND (schizophrenia OR \"eating disorders\" OR adolescents OR OCD OR substance) AND (\"systematic review\" OR \"meta-analysis\" OR \"network meta-analysis\")"]
      ]
    },
    craft: {
      title: "Narrative Translation",
      lede: "These treatment models are useful not only in clinic, but also as lenses for character fate, relationship structure, and dramatic conflict.",
      headers: ["Approach", "Narrative Lens", "Conflict Types"],
      rows: [
        ["CBT / DBT", "How distorted prediction becomes lived reality; how emotion hijacks action", "Shame, fear, avoidance, impulsivity, self-destruction, post-traumatic withdrawal"],
        ["Psychodynamic", "How unresolved past conflict disguises itself as present choice", "Repetition compulsion, attachment, desire and defense, failed intimacy"],
        ["IPT", "How relationship events reorganize the self", "Loss, migration, marriage, parenthood, role transition, social disconnection"],
        ["Systemic / Family", "How symptoms stabilize a group", "Family secrets, scapegoats, alliances, caregiving exhaustion, relapse cycles"]
      ],
      themesTitle: "Reusable clinical motifs",
      themes: [
        "The scapegoat character: one person carries the unspeakable conflict of the whole family.",
        "Repetitive romance: the protagonist keeps falling for the same person in different costumes.",
        "Symptom as loyalty: recovery feels like betrayal because the old relationship system depends on the symptom.",
        "Role transition crisis: graduation, inheritance, migration, marriage, or unemployment destabilizes identity structure.",
        "High expressed-emotion family: supposed care becomes a relapse trigger."
      ]
    },
    works: {
      title: "Art References",
      lede: "These works are useful because they dramatize symptom worlds, relational systems, and repeated fate patterns.",
      items: [
        ["Film", "Good Will Hunting", "A rich reference for attachment trauma, shame defense, and corrective relationship experience.", "https://en.wikipedia.org/wiki/Good_Will_Hunting"],
        ["Film", "Ordinary People", "Excellent for grief, silence, and symptom emergence through IPT and family-systems lenses.", "https://en.wikipedia.org/wiki/Ordinary_People"],
        ["Series", "The Sopranos", "Useful for transference, defense, control, and power in the treatment relationship.", "https://www.hbo.com/the-sopranos"],
        ["Game", "Disco Elysium", "A high-level example of turning inner multiplicity and self-narration into mechanics.", "https://discoelysium.com/"],
        ["Game", "Hellblade: Senua's Sacrifice", "A strong perceptual reference for how psychotic experience can be artistically rendered.", "https://www.hellblade.com/"],
        ["Novel", "The Bell Jar", "Useful for depression, identity constriction, and social role pressure.", "https://en.wikipedia.org/wiki/The_Bell_Jar"]
      ]
    },
    ideas: {
      title: "Story Hooks",
      lede: "These concepts can already serve as seeds for game worlds, scripts, or portfolio concepts.",
      cards: [
        ["Systemic", "The symptom is the family fuse", "A girl with recurrent panic and mutism is actually carrying a secret that keeps the whole family system stable."],
        ["Psychodynamic", "The protagonist always falls for the same person", "Across cities and life stages, the repeated object is less important than the repeated early relational script."],
        ["CBT", "Automatic thoughts rewrite the interface", "Catastrophic prediction warps maps, NPC expressions, and quest text until the player uses exposure and behavioral experiments to recalibrate reality."],
        ["IPT", "After losing the role of being needed", "A long-term caregiver becomes depressed after the death of the person they cared for; the core loss is also a loss of role, structure, and place in the social field."]
      ]
    },
    archive: {
      title: "Reference Archive",
      lede: "The repository includes an auditable archive with bilingual entries, summary notes, open-access links, selected PDFs, citation counts, and journal-ranking fields.",
      items: [
        ["Bilingual reference table", "A quick surface for titles, indications, techniques, citation counts, journal quartiles, and summaries.", "reference_archive/reference_table_bilingual.md"],
        ["Bilingual CSV index", "Useful for spreadsheet filtering, sorting, and later annotation work.", "reference_archive/reference_index_bilingual.csv"],
        ["Open-access index", "Centralized PMC, author manuscript, PDF, and OA link tracking.", "reference_archive/open_access_index.csv"],
        ["BibTeX file", "Ready for writing workflows or citation managers.", "reference_archive/citations.bib"],
        ["Archive README", "Explains the structure, naming system, and available materials.", "reference_archive/README_v2.md"],
        ["Audit summary", "Documents the build and quality-control process for the archive.", "reference_archive/AGENT_AUDIT_SUMMARY.md"]
      ]
    },
    sources: {
      title: "Sources",
      lede: "Only the core spine is listed here; the full archive remains in the reference folder.",
      coreTitle: "Core academic sources",
      extraTitle: "Guidelines and supporting material",
      core: [
        ["Leichsenring et al. 2022", "https://doi.org/10.1017/S0033291721002965"],
        ["Cuijpers et al. 2025", "https://pubmed.ncbi.nlm.nih.gov/40238104/"],
        ["Cuijpers et al. 2016", "https://research.vu.nl/en/publications/interpersonal-psychotherapy-for-mental-health-problems-a-comprehe"],
        ["Wienicke et al. 2023", "https://pubmed.ncbi.nlm.nih.gov/36958077/"],
        ["Rodolico et al. 2022", "https://pubmed.ncbi.nlm.nih.gov/35462002/"],
        ["Cuijpers et al. 2021", "https://pubmed.ncbi.nlm.nih.gov/34135080/"]
      ],
      extra: [
        ["NICE NG222", "https://www.nice.org.uk/guidance/ng222"],
        ["APA Depression Guideline", "https://www.apa.org/depression-guideline"],
        ["Psychotherapies at a Glance", "https://psychiatryonline.org/doi/10.1176/appi.psychotherapy.20230035"],
        ["Shedler 2010", "https://pubmed.ncbi.nlm.nih.gov/20141265/"],
        ["Behavioral Tech DBT FAQ", "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/"]
      ]
    }
  }
};

const bindText = (path, data) => {
  document.querySelectorAll(`[data-bind="${path}"]`).forEach((node) => {
    const parts = path.split(".");
    let value = data;
    for (const part of parts) {
      value = value?.[part];
    }
    node.textContent = value ?? "";
  });
};

const renderLinkList = (items, container) => {
  container.innerHTML = "";
  items.forEach((item) => {
    const link = document.createElement("a");
    link.className = "hero-link";
    link.href = item.href;
    link.textContent = item.label;
    container.appendChild(link);
  });
};

const renderMeta = (items, container) => {
  container.innerHTML = "";
  items.forEach((item) => {
    const span = document.createElement("span");
    span.className = "meta-pill";
    span.textContent = item;
    container.appendChild(span);
  });
};

const renderToc = (items) => {
  const list = document.getElementById("toc-list");
  list.innerHTML = "";
  items.forEach(([id, label]) => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.href = `#${id}`;
    a.textContent = label;
    li.appendChild(a);
    list.appendChild(li);
  });
};

const renderLayerCards = (items) => {
  const grid = document.getElementById("overview-pill-grid");
  grid.innerHTML = "";
  items.forEach(([title, body]) => {
    const article = document.createElement("article");
    article.className = "mini-card";
    article.innerHTML = `<h3>${title}</h3><p>${body}</p>`;
    grid.appendChild(article);
  });
};

const renderCoreCards = (cards) => {
  const grid = document.getElementById("core-card-grid");
  grid.innerHTML = "";
  cards.forEach((card) => {
    const article = document.createElement("article");
    article.className = "card";
    article.innerHTML = `
      <div class="card-tag">${card.tag}</div>
      <h3>${card.title}</h3>
      <p>${card.body}</p>
      <p>${card.links.map((link) => `<a href="${link.href}">${link.label}</a>`).join(" · ")}</p>
    `;
    grid.appendChild(article);
  });
};

const renderTable = (headers, rows, headId, bodyId) => {
  const head = document.getElementById(headId);
  const body = document.getElementById(bodyId);
  head.innerHTML = `<tr>${headers.map((text) => `<th>${text}</th>`).join("")}</tr>`;
  body.innerHTML = rows.map((row) => `<tr>${row.map((cell) => `<td>${cell}</td>`).join("")}</tr>`).join("");
};

const renderSimpleCards = (items, containerId) => {
  const grid = document.getElementById(containerId);
  grid.innerHTML = "";
  items.forEach(([tag, body]) => {
    const article = document.createElement("article");
    article.className = "card";
    article.innerHTML = `<div class="card-tag">${tag}</div><p>${body}</p>`;
    grid.appendChild(article);
  });
};

const renderQueries = (items) => {
  const grid = document.getElementById("query-grid");
  grid.innerHTML = "";
  items.forEach(([title, query]) => {
    const article = document.createElement("article");
    article.className = "query-card";
    article.innerHTML = `<h3>${title}</h3><pre>${query}</pre>`;
    grid.appendChild(article);
  });
};

const renderList = (items, containerId) => {
  const list = document.getElementById(containerId);
  list.innerHTML = "";
  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    list.appendChild(li);
  });
};

const renderWorks = (items) => {
  const grid = document.getElementById("work-grid");
  grid.innerHTML = "";
  items.forEach(([tag, title, body, href]) => {
    const article = document.createElement("article");
    article.className = "work-card";
    article.innerHTML = `
      <div class="work-tag">${tag}</div>
      <h3>${title}</h3>
      <p>${body}</p>
      <p><a href="${href}">${href}</a></p>
    `;
    grid.appendChild(article);
  });
};

const renderIdeaCards = (items) => {
  const grid = document.getElementById("idea-grid");
  grid.innerHTML = "";
  items.forEach(([tag, title, body]) => {
    const article = document.createElement("article");
    article.className = "card";
    article.innerHTML = `<div class="card-tag">${tag}</div><h3>${title}</h3><p>${body}</p>`;
    grid.appendChild(article);
  });
};

const renderArchiveCards = (items) => {
  const grid = document.getElementById("archive-grid");
  grid.innerHTML = "";
  items.forEach(([title, body, href]) => {
    const article = document.createElement("article");
    article.className = "archive-card";
    article.innerHTML = `<h3>${title}</h3><p>${body}</p><p><a href="${href}">${href}</a></p>`;
    grid.appendChild(article);
  });
};

const renderSources = (items, containerId) => {
  const list = document.getElementById(containerId);
  list.innerHTML = "";
  items.forEach(([label, href]) => {
    const li = document.createElement("li");
    li.innerHTML = `<a href="${href}">${label}</a>`;
    list.appendChild(li);
  });
};

const setActiveButton = (lang) => {
  document.querySelectorAll(".lang-button").forEach((button) => {
    button.classList.toggle("is-active", button.dataset.lang === lang);
  });
};

const renderLanguage = (lang) => {
  const data = siteContent[lang] ?? siteContent.zh;
  document.documentElement.lang = data.htmlLang;
  document.title = data.pageTitle;

  bindText("hero.kicker", data);
  bindText("hero.title", data);
  bindText("hero.subtitle", data);
  bindText("toc.title", data);
  bindText("overview.title", data);
  bindText("overview.lede", data);
  bindText("overview.note", data);
  bindText("core.title", data);
  bindText("core.lede", data);
  bindText("map.title", data);
  bindText("map.lede", data);
  bindText("map.note", data);
  bindText("life.title", data);
  bindText("life.lede", data);
  bindText("search.title", data);
  bindText("search.lede", data);
  bindText("craft.title", data);
  bindText("craft.lede", data);
  bindText("craft.themesTitle", data);
  bindText("works.title", data);
  bindText("works.lede", data);
  bindText("ideas.title", data);
  bindText("ideas.lede", data);
  bindText("archive.title", data);
  bindText("archive.lede", data);
  bindText("sources.title", data);
  bindText("sources.lede", data);
  bindText("sources.coreTitle", data);
  bindText("sources.extraTitle", data);

  renderMeta(data.hero.meta, document.getElementById("hero-meta"));
  renderLinkList(data.hero.links, document.getElementById("hero-links"));
  renderToc(data.toc.items);
  renderLayerCards(data.overview.layers);
  renderCoreCards(data.core.cards);
  renderTable(data.map.headers, data.map.rows, "map-head", "map-body");
  renderSimpleCards(data.life.cards, "life-card-grid");
  renderQueries(data.search.items);
  renderTable(data.craft.headers, data.craft.rows, "craft-head", "craft-body");
  renderList(data.craft.themes, "craft-themes");
  renderWorks(data.works.items);
  renderIdeaCards(data.ideas.cards);
  renderArchiveCards(data.archive.items);
  renderSources(data.sources.core, "source-core");
  renderSources(data.sources.extra, "source-extra");
  setActiveButton(lang);
  localStorage.setItem("psychotherapyAtlasLanguage", lang);
};

document.querySelectorAll(".lang-button").forEach((button) => {
  button.addEventListener("click", () => renderLanguage(button.dataset.lang));
});

const savedLanguage = localStorage.getItem("psychotherapyAtlasLanguage");
renderLanguage(savedLanguage === "en" ? "en" : "zh");
