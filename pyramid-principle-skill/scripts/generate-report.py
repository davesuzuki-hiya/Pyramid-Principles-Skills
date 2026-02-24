#!/usr/bin/env python3
"""
Pyramid Principle Interactive Report Generator

Generates an interactive HTML report from structured analysis data.
Usage: python generate-report.py [input.json] [output.html]
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def generate_html_report(data):
    """Generate complete HTML report from structured data"""
    
    title = data.get('title', 'Strategic Analysis Report')
    subtitle = data.get('subtitle', '')
    author = data.get('author', '')
    date = data.get('date', datetime.now().strftime('%B %d, %Y'))
    governing_thought = data.get('governing_thought', '')
    scqa = data.get('scqa', {})
    arguments = data.get('arguments', [])
    hypothesis = data.get('hypothesis', {})
    recommendations = data.get('recommendations', [])
    timeline = data.get('timeline', [])
    
    # Generate SCQA cards
    scqa_html = ''
    for key, label in [('situation', 'Situation'), ('complication', 'Complication'), 
                       ('question', 'Question'), ('answer', 'Answer')]:
        if key in scqa:
            scqa_html += f'''
            <div class="scqa-card {key}">
                <span class="label">{label}</span>
                <p>{scqa[key]}</p>
            </div>'''
    
    # Generate arguments
    args_html = ''
    for i, arg in enumerate(arguments, 1):
        evidence = ''.join([f'<li>{e}</li>' for e in arg.get('evidence', [])])
        so_what = arg.get('so_what', '')
        args_html += f'''
        <div class="argument-card">
            <div class="argument-header">
                <h3>Argument {i}: {arg.get('title', '')}</h3>
                <span class="toggle">▼</span>
            </div>
            <div class="argument-content">
                <p>{arg.get('description', '')}</p>
                <ul class="evidence-list">{evidence}</ul>
                {f'<div class="so-what"><strong>So What:</strong> {so_what}</div>' if so_what else ''}
            </div>
        </div>'''
    
    # Generate proof points
    proof_html = ''
    for pp in hypothesis.get('proof_points', []):
        status = pp.get('status', 'pending').lower()
        icons = {'validated': '✓', 'inconclusive': '?', 'disproved': '✗', 'pending': '○'}
        proof_html += f'''
        <div class="proof-point">
            <span class="status {status}">{icons.get(status, '○')}</span>
            <div>
                <strong>{pp.get('point', '')}</strong>
                <p class="finding">{pp.get('finding', '')}</p>
            </div>
        </div>'''
    
    # Generate recommendations
    recs_html = ''.join([f'<div class="rec-item"><strong>{i+1}.</strong> {r}</div>' 
                         for i, r in enumerate(recommendations)])
    
    # Generate timeline
    timeline_html = ''.join([f'''
        <div class="timeline-item">
            <div class="date">{t.get('date', '')}</div>
            <div class="title">{t.get('title', '')}</div>
            <p class="desc">{t.get('description', '')}</p>
        </div>''' for t in timeline])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #1e3a5f;
            --secondary: #3d5a80;
            --accent: #ee6c4d;
            --success: #2d6a4f;
            --warning: #e9c46a;
            --danger: #e76f51;
            --bg: #f8f9fa;
            --text: #293241;
            --text-light: #5c677d;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', -apple-system, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e8ec 100%);
            color: var(--text);
            line-height: 1.6;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
        
        .header {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            padding: 3rem 2rem;
            border-radius: 16px;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(30, 58, 95, 0.3);
        }}
        .header h1 {{ font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem; }}
        .header .subtitle {{ font-size: 1.1rem; opacity: 0.9; }}
        .header .meta {{ display: flex; gap: 2rem; margin-top: 1.5rem; font-size: 0.9rem; opacity: 0.8; }}
        
        .exec-summary {{
            background: white;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            border-left: 5px solid var(--accent);
        }}
        .exec-summary h2 {{
            color: var(--accent);
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-bottom: 1rem;
        }}
        .governing-thought {{
            font-size: 1.4rem;
            font-weight: 600;
            color: var(--primary);
            line-height: 1.4;
        }}
        
        .scqa-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }}
        .scqa-card {{
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
            transition: transform 0.2s;
        }}
        .scqa-card:hover {{ transform: translateY(-4px); }}
        .scqa-card .label {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
        }}
        .scqa-card.situation .label {{ background: #e3f2fd; color: #1565c0; }}
        .scqa-card.complication .label {{ background: #fff3e0; color: #e65100; }}
        .scqa-card.question .label {{ background: #f3e5f5; color: #7b1fa2; }}
        .scqa-card.answer .label {{ background: #e8f5e9; color: #2e7d32; }}
        
        .section-title {{
            font-size: 1.5rem;
            font-weight: 600;
            color: var(--primary);
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        .section-title::before {{
            content: '';
            width: 4px;
            height: 1.5rem;
            background: var(--accent);
            border-radius: 2px;
        }}
        
        .argument-card {{
            background: white;
            border-radius: 12px;
            margin-bottom: 1rem;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        }}
        .argument-header {{
            padding: 1.5rem;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-left: 4px solid var(--secondary);
            transition: background 0.2s;
        }}
        .argument-header:hover {{ background: var(--bg); }}
        .argument-header h3 {{ font-size: 1.1rem; color: var(--primary); }}
        .argument-header .toggle {{ font-size: 1.5rem; color: var(--secondary); transition: transform 0.3s; }}
        .argument-card.expanded .toggle {{ transform: rotate(180deg); }}
        .argument-content {{
            display: none;
            padding: 0 1.5rem 1.5rem;
            border-top: 1px solid #eee;
        }}
        .argument-card.expanded .argument-content {{ display: block; }}
        .evidence-list {{ list-style: none; margin-top: 1rem; }}
        .evidence-list li {{
            padding: 0.75rem 1rem;
            background: var(--bg);
            border-radius: 8px;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
        }}
        .evidence-list li::before {{ content: '✓'; color: var(--success); font-weight: bold; }}
        .so-what {{
            margin-top: 1rem;
            padding: 1rem;
            background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
            border-radius: 8px;
            border-left: 3px solid var(--success);
        }}
        .so-what strong {{ color: var(--success); }}
        
        .hypothesis-section {{
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        }}
        .hypothesis-statement {{
            background: var(--bg);
            padding: 1rem;
            border-radius: 8px;
            font-style: italic;
            margin-bottom: 1.5rem;
        }}
        .proof-point {{
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1rem;
            background: var(--bg);
            border-radius: 8px;
            margin-bottom: 0.5rem;
        }}
        .proof-point .status {{
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            color: white;
            flex-shrink: 0;
        }}
        .proof-point .status.validated {{ background: var(--success); }}
        .proof-point .status.inconclusive {{ background: var(--warning); color: var(--text); }}
        .proof-point .status.disproved {{ background: var(--danger); }}
        .proof-point .status.pending {{ background: #ccc; }}
        .proof-point .finding {{ font-size: 0.9rem; color: var(--text-light); margin-top: 0.25rem; }}
        
        .recommendations {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            border-radius: 12px;
            padding: 2rem;
            color: white;
            margin-bottom: 2rem;
        }}
        .recommendations h2 {{ font-size: 1.5rem; margin-bottom: 1.5rem; }}
        .rec-item {{
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 0.75rem;
        }}
        .rec-item strong {{ color: var(--warning); }}
        
        .timeline {{
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        }}
        .timeline-items {{ position: relative; margin-top: 1.5rem; }}
        .timeline-items::before {{
            content: '';
            position: absolute;
            left: 15px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, var(--accent), var(--success));
        }}
        .timeline-item {{ position: relative; padding-left: 3rem; padding-bottom: 1.5rem; }}
        .timeline-item::before {{
            content: '';
            position: absolute;
            left: 8px;
            top: 0;
            width: 16px;
            height: 16px;
            background: var(--accent);
            border-radius: 50%;
            border: 3px solid white;
            box-shadow: 0 2px 8px rgba(238, 108, 77, 0.3);
        }}
        .timeline-item .date {{ font-size: 0.85rem; color: var(--text-light); }}
        .timeline-item .title {{ font-weight: 600; color: var(--primary); }}
        .timeline-item .desc {{ font-size: 0.9rem; color: var(--text-light); }}
        
        .footer {{ text-align: center; padding: 2rem; color: var(--text-light); font-size: 0.85rem; }}
        
        @media (max-width: 768px) {{
            .container {{ padding: 1rem; }}
            .header {{ padding: 2rem 1.5rem; }}
            .header h1 {{ font-size: 1.75rem; }}
            .scqa-grid {{ grid-template-columns: 1fr; }}
        }}
        @media print {{
            .argument-content {{ display: block !important; }}
            .toggle {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p class="subtitle">{subtitle}</p>
            <div class="meta">
                <span>📅 {date}</span>
                {f'<span>👤 {author}</span>' if author else ''}
            </div>
        </div>

        <div class="exec-summary">
            <h2>Executive Summary</h2>
            <p class="governing-thought">{governing_thought}</p>
        </div>

        <div class="scqa-grid">{scqa_html}</div>

        <div class="arguments-section">
            <h2 class="section-title">Key Arguments</h2>
            {args_html}
        </div>

        {f'''
        <div class="hypothesis-section">
            <h2 class="section-title">Hypothesis Validation</h2>
            <div class="hypothesis-statement">"{hypothesis.get('statement', '')}"</div>
            {proof_html}
        </div>
        ''' if hypothesis else ''}

        {f'''
        <div class="recommendations">
            <h2>Recommendations</h2>
            {recs_html}
        </div>
        ''' if recommendations else ''}

        {f'''
        <div class="timeline">
            <h2 class="section-title">Implementation Timeline</h2>
            <div class="timeline-items">{timeline_html}</div>
        </div>
        ''' if timeline else ''}

        <div class="footer">
            <p>Generated using Pyramid Principle Skill • {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </div>
    </div>

    <script>
        document.querySelectorAll('.argument-header').forEach(header => {{
            header.addEventListener('click', () => {{
                header.parentElement.classList.toggle('expanded');
            }});
        }});
        const firstArg = document.querySelector('.argument-card');
        if (firstArg) firstArg.classList.add('expanded');
    </script>
</body>
</html>'''


EXAMPLE_DATA = {
    "title": "PLG Conversion Optimization Strategy",
    "subtitle": "Recommendations for Q1 2026 Initiative",
    "author": "Product Team",
    "date": "February 2026",
    "governing_thought": "Hiya must implement usage-based pricing within Q2 to capture the price-sensitive SMB segment and increase conversion rates by 200%.",
    "scqa": {
        "situation": "Hiya's PLG product has achieved 2M downloads with strong retention metrics.",
        "complication": "Conversion from free to paid is 0.8%—well below the 3% benchmark—leaving $6M annually on the table.",
        "question": "How can we unlock this value without cannibalizing existing premium subscribers?",
        "answer": "Introduce usage-based pricing that captures value-realized users at their moment of highest intent."
    },
    "arguments": [
        {
            "title": "The Conversion Gap is a Pricing Problem",
            "description": "Analysis of churned trials reveals price sensitivity as the primary barrier.",
            "evidence": [
                "67% of churned trials cite 'price' as primary barrier (n=500)",
                "Users with >20 blocked calls convert at 4x average rate",
                "Binary pricing (free vs $9.99) misses moderate users"
            ],
            "so_what": "A mid-tier option would capture the 'convinced but cost-sensitive' segment."
        },
        {
            "title": "Usage-Based Pricing Aligns Value with Revenue",
            "description": "Consumption models work for PLG leaders like Twilio and AWS.",
            "evidence": [
                "Successful PLG companies use consumption models",
                "Clear value inflection at 50 blocked calls/month",
                "Model: First 50 free, then $0.10/block or $4.99/month unlimited"
            ],
            "so_what": "Users pay only when they've experienced value."
        },
        {
            "title": "Implementation Risk is Low, Upside is High",
            "description": "Technical feasibility and financial modeling support controlled rollout.",
            "evidence": [
                "Engineering estimate: 4 weeks",
                "$2.4M incremental revenue projected, 12% cannibalization",
                "A/B test framework enables controlled validation"
            ],
            "so_what": "Validate hypothesis with minimal investment before full launch."
        }
    ],
    "hypothesis": {
        "statement": "Usage-based pricing will increase conversion by capturing price-sensitive users.",
        "proof_points": [
            {"point": "Price is primary barrier", "status": "validated", "finding": "67% cite price"},
            {"point": "$4.99 is acceptable", "status": "validated", "finding": "68% acceptance"},
            {"point": "Features differentiated", "status": "inconclusive", "finding": "Overlap with Premium"},
            {"point": "Cannibalization manageable", "status": "disproved", "finding": "35% cannibalization"},
            {"point": "Implementation feasible", "status": "validated", "finding": "3 weeks estimate"}
        ]
    },
    "recommendations": [
        "Pivot to usage-based pricing (not fixed tiers)",
        "Implement 'First 50 blocks free, then $0.10/block'",
        "A/B test with 10% traffic in Week 7-8",
        "Full rollout if >2% conversion, <15% cannibalization"
    ],
    "timeline": [
        {"date": "Week 1-2", "title": "Finalize Pricing Model", "description": "Work with Finance on unit economics"},
        {"date": "Week 3-6", "title": "Engineering Build", "description": "Implement pricing and checkout"},
        {"date": "Week 7-8", "title": "A/B Test", "description": "10% traffic test"},
        {"date": "Week 9-12", "title": "Full Rollout", "description": "Scale if metrics positive"}
    ]
}


def main():
    if len(sys.argv) < 2:
        print("Generating example report...")
        html = generate_html_report(EXAMPLE_DATA)
        output = Path('pyramid-report.html')
    else:
        input_path = Path(sys.argv[1])
        with open(input_path) as f:
            data = json.load(f)
        html = generate_html_report(data)
        output = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix('.html')
    
    with open(output, 'w') as f:
        f.write(html)
    print(f"Report generated: {output}")


if __name__ == '__main__':
    main()
