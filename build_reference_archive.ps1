$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$root = Join-Path $PSScriptRoot "reference_archive"
$downloads = Join-Path $root "_downloads"

$sources = @(
  [pscustomobject]@{
    citation_id = "core_umbrella_2022_leichsenring"
    folder = "01_core_evidence"
    subfolder = "general_psychotherapy"
    file_stem = "2022_Leichsenring_UmbrellaReview_GeneralPsychotherapy"
    title = "The efficacy of psychotherapies and pharmacotherapies for mental disorders in adults: an umbrella review and meta-analytic evaluation of recent meta-analyses"
    chinese_title = ""
    authors = "Leichsenring F; Steinert C; Rabung S; Ioannidis JPA; et al."
    year = "2022"
    journal = "World Psychiatry"
    source_type = "Journal article"
    study_design = "Umbrella review"
    therapy_modality = "Cross-modality psychotherapy"
    target_condition = "Adult mental disorders"
    evidence_level = "High"
    display_tier = "core_evidence"
    can_be_used_as_core_evidence = "yes"
    doi = "10.1002/wps.20941"
    pmid = ""
    url = "https://doi.org/10.1002/wps.20941"
    open_url = "https://pubmed.ncbi.nlm.nih.gov/?term=10.1002/wps.20941"
    why_included = "Top-level evidence map for overall modality-by-indication reasoning."
    main_outcomes = "Across disorders, psychotherapy is effective overall; CBT has the broadest evidence base, while modality-specific strengths differ by condition."
    applicability_to_practice = "Use for the overall map, not as a substitute for diagnosis-specific reviews."
    named_techniques_or_components = "Cross-modality overview rather than a single technique package."
    indication_scope = "Adult psychiatric disorders"
    limitations = "High-level synthesis with heterogeneity across diagnoses and modalities."
    risk_of_bias_or_caveat = "Depends on the quality of underlying meta-analyses."
  }
  [pscustomobject]@{
    citation_id = "core_cbt_2025_cuijpers"
    folder = "01_core_evidence"
    subfolder = "cbt"
    file_stem = "2025_Cuijpers_MetaAnalyses_CBT_Adults"
    title = "Cognitive Behavior Therapy for Mental Disorders in Adults"
    chinese_title = ""
    authors = "Cuijpers P; Miguel C; Ciharova M; et al."
    year = "2025"
    journal = "JAMA Psychiatry"
    source_type = "Journal article"
    study_design = "Unified series of meta-analyses"
    therapy_modality = "CBT"
    target_condition = "Adult mental disorders"
    evidence_level = "High"
    display_tier = "core_evidence"
    can_be_used_as_core_evidence = "yes"
    doi = "10.1001/jamapsychiatry.2025.0482"
    pmid = "40238104"
    url = "https://doi.org/10.1001/jamapsychiatry.2025.0482"
    open_url = "https://pubmed.ncbi.nlm.nih.gov/40238104/"
    why_included = "High-quality CBT panorama used to support technique-by-indication mapping."
    main_outcomes = "CBT shows stable efficacy across depression, anxiety spectrum, trauma-related disorders, OCD, and other structured symptom syndromes."
    applicability_to_practice = "Supports cognitive restructuring, exposure, behavioral activation, and behavioral experiments."
    named_techniques_or_components = "Cognitive restructuring; exposure; behavioral activation; behavioral experiments; problem solving."
    indication_scope = "Adults; multiple disorders"
    limitations = "Broad scope, but subgroup, comorbidity, and longer-term questions still need targeted reviews."
    risk_of_bias_or_caveat = "Study quality and comparators differ across disorders."
  }
  [pscustomobject]@{
    citation_id = "core_ipt_2016_cuijpers"
    folder = "01_core_evidence"
    subfolder = "ipt"
    file_stem = "2016_Cuijpers_MetaAnalysis_IPT_MentalHealth"
    title = "Interpersonal Psychotherapy for Mental Health Problems: A Comprehensive Meta-Analysis"
    chinese_title = ""
    authors = "Cuijpers P; Donker T; Weissman MM; Ravitz P; Cristea IA"
    year = "2016"
    journal = "American Journal of Psychiatry"
    source_type = "Journal article"
    study_design = "Comprehensive meta-analysis"
    therapy_modality = "IPT"
    target_condition = "Mental health problems, especially depression"
    evidence_level = "High"
    display_tier = "core_evidence"
    can_be_used_as_core_evidence = "yes"
    doi = "10.1176/appi.ajp.2015.15091141"
    pmid = ""
    url = "https://doi.org/10.1176/appi.ajp.2015.15091141"
    open_url = "https://research.vu.nl/en/publications/interpersonal-psychotherapy-for-mental-health-problems-a-comprehe"
    why_included = "Representative IPT review for depression and relationship-event-linked indications."
    main_outcomes = "Strongest evidence for depression, including adult and perinatal contexts; promising extensions to other conditions."
    applicability_to_practice = "Supports grief work, role transition work, interpersonal dispute work, and social support rebuilding."
    named_techniques_or_components = "Role transition work; grief work; interpersonal disputes; communication analysis; social support rebuilding."
    indication_scope = "Depression-focused, with broader mental health applications"
    limitations = "Evidence outside depression is thinner than for CBT."
    risk_of_bias_or_caveat = "Strength drops when extended beyond depression."
  }
  [pscustomobject]@{
    citation_id = "core_pdt_2023_wienicke"
    folder = "01_core_evidence"
    subfolder = "psychodynamic"
    file_stem = "2023_Wienicke_SystematicReview_MetaAnalysis_Psychodynamic_Depression"
    title = "Efficacy and moderators of short-term psychodynamic psychotherapy for depression: A systematic review and meta-analysis of individual participant data"
    chinese_title = ""
    authors = "Wienicke FJ; Beutel ME; Zwerenz R; et al."
    year = "2023"
    journal = "Clinical Psychology Review"
    source_type = "Journal article"
    study_design = "Systematic review and meta-analysis of individual participant data"
    therapy_modality = "Psychodynamic therapy / STPP"
    target_condition = "Depression"
    evidence_level = "High"
    display_tier = "core_evidence"
    can_be_used_as_core_evidence = "yes"
    doi = "10.1016/j.cpr.2023.102269"
    pmid = "36958077"
    url = "https://doi.org/10.1016/j.cpr.2023.102269"
    open_url = "https://pubmed.ncbi.nlm.nih.gov/36958077/"
    why_included = "Key evidence source for psychodynamic treatment in depression."
    main_outcomes = "Short-term psychodynamic psychotherapy is efficacious for depression, with clinically useful moderator analyses from IPD synthesis."
    applicability_to_practice = "Supports affect focus, defense analysis, relationship-theme work, and transference work."
    named_techniques_or_components = "Clarification; confrontation; interpretation; defense analysis; affect focus; transference work."
    indication_scope = "Depression, especially patterns tied to recurring relational conflicts"
    limitations = "Focused on depression rather than all complex personality presentations."
    risk_of_bias_or_caveat = "Therapist factors and treatment fidelity may still affect results."
  }
  [pscustomobject]@{
    citation_id = "core_family_2022_rodolico"
    folder = "01_core_evidence"
    subfolder = "family_intervention_schizophrenia"
    file_stem = "2022_Rodolico_NetworkMeta_FamilyIntervention_Schizophrenia"
    title = "Family interventions for relapse prevention in schizophrenia: a systematic review and network meta-analysis"
    chinese_title = ""
    authors = "Rodolico A; Bighelli I; Avanzato C; et al."
    year = "2022"
    journal = "The Lancet Psychiatry"
    source_type = "Journal article"
    study_design = "Systematic review and network meta-analysis"
    therapy_modality = "Family intervention / systemic family treatment"
    target_condition = "Schizophrenia relapse prevention"
    evidence_level = "High"
    display_tier = "core_evidence"
    can_be_used_as_core_evidence = "yes"
    doi = "10.1016/S2215-0366(21)00437-5"
    pmid = ""
    url = "https://doi.org/10.1016/S2215-0366(21)00437-5"
    open_url = "https://pubmed.ncbi.nlm.nih.gov/?term=10.1016%2FS2215-0366(21)00437-5"
    why_included = "Key evidence source for systemic/family treatment in a strong indication area."
    main_outcomes = "Family interventions reduce relapse-related outcomes in schizophrenia and support psychoeducation plus communication-focused work."
    applicability_to_practice = "Supports psychoeducation, communication training, problem solving, and relapse warning management."
    named_techniques_or_components = "Psychoeducation; communication training; problem solving; relapse warning management."
    indication_scope = "Schizophrenia spectrum relapse prevention"
    limitations = "Does not imply equal strength for family therapy across all adult disorders."
    risk_of_bias_or_caveat = "Intervention packages vary in content and intensity."
  }
  [pscustomobject]@{
    citation_id = "core_depression_nma_2021_cuijpers"
    folder = "01_core_evidence"
    subfolder = "depression_cross_modality"
    file_stem = "2021_Cuijpers_NetworkMeta_Psychotherapies_Depression"
    title = "Psychotherapies for depression: a network meta-analysis covering efficacy, acceptability and long-term outcomes of all main treatment types"
    chinese_title = ""
    authors = "Cuijpers P; Karyotaki E; de Wit L; Ebert DD"
    year = "2021"
    journal = "World Psychiatry"
    source_type = "Journal article"
    study_design = "Network meta-analysis"
    therapy_modality = "Multiple psychotherapy modalities"
    target_condition = "Depression"
    evidence_level = "High"
    display_tier = "core_evidence"
    can_be_used_as_core_evidence = "yes"
    doi = "10.1002/wps.20860"
    pmid = ""
    url = "https://doi.org/10.1002/wps.20860"
    open_url = "https://pubmed.ncbi.nlm.nih.gov/?term=10.1002%2Fwps.20860"
    why_included = "Key cross-modality comparison source for depression."
    main_outcomes = "Major depression can be treated effectively by several psychotherapy families, with differences in acceptability and longer-term data across modalities."
    applicability_to_practice = "Helps compare CBT, behavioral activation, IPT, and psychodynamic approaches in depression."
    named_techniques_or_components = "Cross-modality comparison rather than a single technique manual."
    indication_scope = "Depression in adults"
    limitations = "Indirect comparisons do not replace head-to-head trial detail."
    risk_of_bias_or_caveat = "Comparators and sample features vary across trials."
  }
  [pscustomobject]@{
    citation_id = "guideline_nice_2022_depression"
    folder = "02_guidelines"
    subfolder = "depression"
    file_stem = "2022_NICE_Guideline_DepressionAdults"
    title = "Depression in adults: treatment and management (NG222)"
    chinese_title = ""
    authors = "National Institute for Health and Care Excellence"
    year = "2022"
    journal = "NICE Guideline"
    source_type = "Guideline"
    study_design = "Clinical guideline"
    therapy_modality = "Multiple psychotherapy modalities"
    target_condition = "Depression"
    evidence_level = "High"
    display_tier = "core_guideline"
    can_be_used_as_core_evidence = "yes"
    doi = ""
    pmid = ""
    url = "https://www.nice.org.uk/guidance/ng222"
    open_url = "https://www.nice.org.uk/guidance/ng222"
    why_included = "Mainstream guideline used to check recommendation strength and ordering in depression."
    main_outcomes = "Recommends evidence-based psychotherapies such as CBT, behavioral activation, IPT, and short-term psychodynamic approaches depending on severity and preference."
    applicability_to_practice = "Translates research evidence into clinical pathway language."
    named_techniques_or_components = "Guideline-level modality recommendations."
    indication_scope = "Adult depression care pathway"
    limitations = "Focused on the UK healthcare pathway."
    risk_of_bias_or_caveat = "Normative synthesis, not primary research."
  }
  [pscustomobject]@{
    citation_id = "guideline_apa_2019_depression"
    folder = "02_guidelines"
    subfolder = "depression"
    file_stem = "2019_APA_Guideline_DepressionAcrossThreeAgeCohorts"
    title = "Clinical Practice Guideline for the Treatment of Depression Across Three Age Cohorts"
    chinese_title = ""
    authors = "American Psychological Association"
    year = "2019"
    journal = "APA Guideline"
    source_type = "Guideline"
    study_design = "Clinical practice guideline"
    therapy_modality = "Multiple psychotherapy modalities"
    target_condition = "Depression"
    evidence_level = "High"
    display_tier = "core_guideline"
    can_be_used_as_core_evidence = "yes"
    doi = ""
    pmid = ""
    url = "https://www.apa.org/depression-guideline"
    open_url = "https://www.apa.org/depression-guideline/guideline.pdf"
    why_included = "Important US guideline used to cross-check NICE."
    main_outcomes = "Supports evidence-based psychotherapy for depression across age groups within structured clinical decision-making."
    applicability_to_practice = "Useful for comparing recommendation logic across systems."
    named_techniques_or_components = "Guideline-level treatment recommendations."
    indication_scope = "Depression across age cohorts"
    limitations = "Depression-focused rather than a full cross-diagnostic guideline."
    risk_of_bias_or_caveat = "Guideline quality depends on the evidence review and consensus procedure."
  }
  [pscustomobject]@{
    citation_id = "support_ataglance_2024"
    folder = "03_supporting_overviews"
    subfolder = "general_psychotherapy"
    file_stem = "2024_AJPsychotherapy_AtAGlance_AdultsPsychiatricDisorders"
    title = "Psychotherapies at a Glance: Consensus Guideline-Recommended Psychotherapies for Adults With Psychiatric Disorders"
    chinese_title = ""
    authors = "American Journal of Psychotherapy article"
    year = "2024"
    journal = "American Journal of Psychotherapy"
    source_type = "Journal article"
    study_design = "Guideline summary / overview"
    therapy_modality = "Multiple psychotherapy modalities"
    target_condition = "Adult psychiatric disorders"
    evidence_level = "Moderate"
    display_tier = "supporting_overview"
    can_be_used_as_core_evidence = "no"
    doi = "10.1176/appi.psychotherapy.20230004"
    pmid = ""
    url = "https://doi.org/10.1176/appi.psychotherapy.20230004"
    open_url = "https://psychiatryonline.org/doi/10.1176/appi.psychotherapy.20230004"
    why_included = "Useful navigation summary for therapy-by-disorder guideline patterns."
    main_outcomes = "Summarizes which psychotherapies are guideline-supported across common adult psychiatric disorders."
    applicability_to_practice = "Helpful as a map, not as a replacement for source guidelines or meta-analyses."
    named_techniques_or_components = "Overview-level summary."
    indication_scope = "Adults with psychiatric disorders"
    limitations = "Secondary overview rather than a new systematic review."
    risk_of_bias_or_caveat = "Evidence depth is lower than original reviews and guidelines."
  }
  [pscustomobject]@{
    citation_id = "theory_shedler_2010"
    folder = "04_theory_and_perspective"
    subfolder = "psychodynamic"
    file_stem = "2010_Shedler_Review_PsychodynamicPsychotherapy"
    title = "The efficacy of psychodynamic psychotherapy"
    chinese_title = ""
    authors = "Shedler J"
    year = "2010"
    journal = "American Psychologist"
    source_type = "Journal article"
    study_design = "Review / perspective"
    therapy_modality = "Psychodynamic therapy"
    target_condition = "Cross-diagnostic discussion"
    evidence_level = "Supplementary"
    display_tier = "theory_or_perspective"
    can_be_used_as_core_evidence = "no"
    doi = "10.1037/a0018378"
    pmid = "20141265"
    url = "https://doi.org/10.1037/a0018378"
    open_url = "https://pubmed.ncbi.nlm.nih.gov/20141265/"
    why_included = "Useful for theory, framing, and historical debate, not for top-tier evidence claims."
    main_outcomes = "Argues psychodynamic psychotherapy is efficacious and often misunderstood in public discourse."
    applicability_to_practice = "Good for explaining the modality, not for evidence ranking."
    named_techniques_or_components = "Psychodynamic concepts overview."
    indication_scope = "General theory"
    limitations = "Not a recent systematic review."
    risk_of_bias_or_caveat = "Should not be displayed on the same evidence tier as recent meta-analyses."
  }
  [pscustomobject]@{
    citation_id = "official_dbt_faq"
    folder = "05_official_explainers"
    subfolder = "dbt"
    file_stem = "BehavioralTech_DBT_FAQ"
    title = "Dialectical Behavior Therapy (DBT) FAQ"
    chinese_title = ""
    authors = "Behavioral Tech"
    year = "n.d."
    journal = "Official organization resource"
    source_type = "Official FAQ"
    study_design = "Institutional explainer"
    therapy_modality = "DBT"
    target_condition = "Emotion dysregulation, self-harm, BPD-related presentations"
    evidence_level = "Supplementary"
    display_tier = "official_explainer"
    can_be_used_as_core_evidence = "no"
    doi = ""
    pmid = ""
    url = "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/"
    open_url = "https://behavioraltech.org/resources/faqs/dialectical-behavior-therapy-dbt/"
    why_included = "Useful for explaining the structure of DBT as a treatment package."
    main_outcomes = "Explains what DBT is and how skills-based, multi-component treatment is structured."
    applicability_to_practice = "Useful for concept clarification, not for evidence ranking."
    named_techniques_or_components = "Mindfulness; distress tolerance; emotion regulation; interpersonal effectiveness."
    indication_scope = "DBT-oriented practice explanation"
    limitations = "Not an academic review."
    risk_of_bias_or_caveat = "Institutional explainer; exclude from evidence-strength rankings."
  }
)

$dirs = @(
  $root,
  $downloads,
  (Join-Path $root "01_core_evidence\general_psychotherapy"),
  (Join-Path $root "01_core_evidence\cbt"),
  (Join-Path $root "01_core_evidence\ipt"),
  (Join-Path $root "01_core_evidence\psychodynamic"),
  (Join-Path $root "01_core_evidence\family_intervention_schizophrenia"),
  (Join-Path $root "01_core_evidence\depression_cross_modality"),
  (Join-Path $root "02_guidelines\depression"),
  (Join-Path $root "03_supporting_overviews\general_psychotherapy"),
  (Join-Path $root "04_theory_and_perspective\psychodynamic"),
  (Join-Path $root "05_official_explainers\dbt")
)

foreach ($dir in $dirs) {
  New-Item -ItemType Directory -Path $dir -Force | Out-Null
}

function New-UrlShortcut {
  param(
    [string]$Path,
    [string]$Url
  )
  $content = @"
[InternetShortcut]
URL=$Url
"@
  Set-Content -LiteralPath $Path -Value $content -Encoding ASCII
}

function Get-Bibtex {
  param(
    [string]$Doi,
    [string]$Key,
    [string]$Title,
    [string]$Authors,
    [string]$Year,
    [string]$Journal,
    [string]$Url
  )
  if ([string]::IsNullOrWhiteSpace($Doi)) {
    if ([string]::IsNullOrWhiteSpace($Key)) {
      return $null
    }
    return "@misc{$Key,`n  title = {$Title},`n  author = {$Authors},`n  year = {$Year},`n  howpublished = {\url{$Url}}`n}"
  }
  try {
    $encoded = [uri]::EscapeDataString($Doi)
    $resp = Invoke-WebRequest -Uri "https://doi.org/$encoded" -Headers @{
      "Accept" = "application/x-bibtex"
      "User-Agent" = "CodexAgent/1.0 (mailto:none@example.com)"
    }
    return ($resp.Content.Trim())
  } catch {
    if ([string]::IsNullOrWhiteSpace($Key)) {
      return $null
    }
    return "@article{$Key,`n  title = {$Title},`n  author = {$Authors},`n  journal = {$Journal},`n  year = {$Year},`n  doi = {$Doi},`n  url = {$Url}`n}"
  }
}

$csvRows = New-Object System.Collections.Generic.List[object]
$bibEntries = New-Object System.Collections.Generic.List[string]

foreach ($src in $sources) {
  $targetDir = Join-Path $root (Join-Path $src.folder $src.subfolder)
  $notePath = Join-Path $targetDir ($src.file_stem + ".md")
  $urlPath = Join-Path $targetDir ($src.file_stem + ".url")

  $note = @"
# $($src.title)

## Citation Card

- citation_id: $($src.citation_id)
- authors: $($src.authors)
- year: $($src.year)
- journal_or_source: $($src.journal)
- source_type: $($src.source_type)
- study_design: $($src.study_design)
- therapy_modality: $($src.therapy_modality)
- target_condition: $($src.target_condition)
- evidence_level: $($src.evidence_level)
- display_tier: $($src.display_tier)
- can_be_used_as_core_evidence: $($src.can_be_used_as_core_evidence)
- doi: $($src.doi)
- pmid: $($src.pmid)
- primary_url: $($src.url)
- secondary_or_open_url: $($src.open_url)

## Why Included

$($src.why_included)

## One-Sentence Takeaway

$($src.main_outcomes)

## Practical Use

$($src.applicability_to_practice)

## Named Techniques / Components

$($src.named_techniques_or_components)

## Indication Scope

$($src.indication_scope)

## Limitations

$($src.limitations)

## Quality Note

$($src.risk_of_bias_or_caveat)
"@

  Set-Content -LiteralPath $notePath -Value $note -Encoding UTF8
  New-UrlShortcut -Path $urlPath -Url $src.url

  $csvRows.Add([pscustomobject]@{
    citation_id = $src.citation_id
    folder = $src.folder
    subfolder = $src.subfolder
    file_stem = $src.file_stem
    year = $src.year
    title = $src.title
    source_type = $src.source_type
    study_design = $src.study_design
    therapy_modality = $src.therapy_modality
    target_condition = $src.target_condition
    evidence_level = $src.evidence_level
    display_tier = $src.display_tier
    can_be_used_as_core_evidence = $src.can_be_used_as_core_evidence
    journal_or_source = $src.journal
    doi = $src.doi
    pmid = $src.pmid
    primary_url = $src.url
    open_url = $src.open_url
  })

  $bib = Get-Bibtex -Doi $src.doi -Key $src.citation_id -Title $src.title -Authors $src.authors -Year $src.year -Journal $src.journal -Url $src.url
  if ($bib) {
    $bibEntries.Add($bib)
  }
}

$readme = @"
# Reference Archive

This folder stores the sources actually used in the psychotherapy research pack and separates them by evidence tier.

## Folder Logic

- 01_core_evidence: umbrella reviews, systematic reviews, meta-analyses, and network meta-analyses that can support core claims.
- 02_guidelines: NICE and APA guideline-level sources.
- 03_supporting_overviews: helpful summaries that are still secondary to the main evidence base.
- 04_theory_and_perspective: theory or perspective pieces; useful, but not to be ranked beside meta-analyses.
- 05_official_explainers: official organization pages for concept clarification, not for evidence ranking.

## Quality Check

If you want to audit citation quality quickly, start with:

1. reference_index.csv
2. 01_core_evidence
3. 02_guidelines
4. citations.bib

Each source has:

- one Markdown citation card
- one .url shortcut
- one row in reference_index.csv
- one BibTeX entry in citations.bib when a DOI was available

## Note

Non-academic creative references were intentionally kept out of this archive so they do not mix with the evidence chain.
"@

Set-Content -LiteralPath (Join-Path $root "README.md") -Value $readme -Encoding UTF8
$csvRows | Export-Csv -LiteralPath (Join-Path $root "reference_index.csv") -NoTypeInformation -Encoding UTF8
if ($bibEntries.Count -gt 0) {
  ($bibEntries -join "`r`n`r`n") + "`r`n" | Set-Content -LiteralPath (Join-Path $root "citations.bib") -Encoding UTF8
}

try {
  Invoke-WebRequest -Uri "https://www.apa.org/depression-guideline/guideline.pdf" -OutFile (Join-Path $downloads "APA_Depression_Guideline.pdf")
} catch {
}

try {
  Invoke-WebRequest -Uri "https://www.apa.org/depression-guideline" -OutFile (Join-Path $downloads "APA_Depression_Guideline_Landing.html")
} catch {
}

try {
  Invoke-WebRequest -Uri "https://www.nice.org.uk/guidance/ng222" -OutFile (Join-Path $downloads "NICE_NG222_Landing.html")
} catch {
}
