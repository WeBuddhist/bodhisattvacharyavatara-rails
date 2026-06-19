import json, re

with open('0-INBOX/.stage2-scratch/batch_03.json', encoding='utf-8') as f:
    data = json.load(f)

decisions = {}

def keep(i, reason):
    decisions[i] = ([], reason)

def split_after(i, markers, reason):
    decisions[i] = (markers, reason)

# 0
keep(0, "single clause giving one example, no internal shift")
# 1: long causal chain - took rebirth/vow -> didn't practice -> regret -> burning torment.
# Defensible split between "generated regret" and the vivid burning-torment consequence.
split_after(1, ["དེ་ལ་འགྱོད་སེམས་བསྐྱེད་དེ་"],
            "shift from stating the failure/regret to describing its burning-torment consequence")
keep(2, "single clause, indivisible")
keep(3, "single conditional clause, indivisible")
keep(4, "single clause, indivisible")
keep(5, "single clause, indivisible")
keep(6, "single simile clause, indivisible")
keep(7, "single clause, indivisible")
keep(8, "single clause, indivisible")
keep(9, "single clause, indivisible")
keep(10, "single clause, indivisible")
keep(11, "single clause, indivisible")
keep(12, "single temporal-frame clause, indivisible")
split_after(13, ["དེའི་སྒོ་ནས་ང་རྒྱལ་ལམ་ཁོང་ཁྲོ་དེ་གོང་ནས་གོང་དུ་འཕེལ་ཞིང་བདོ་བར་གྱུར་པའི་"],
            "shift from anger-escalation description to its behavioral consequence (no peace until revenge)")
keep(14, "single clause, indivisible")
keep(15, "single clause leading into next block, indivisible")
keep(16, "single clause, indivisible")
keep(17, "single clause, indivisible")
keep(18, "single clause, indivisible")
keep(19, "single clause, indivisible")
keep(20, "single clause, indivisible")
keep(21, "single purpose clause, indivisible")
keep(22, "single clause, indivisible")
keep(23, "single clause, indivisible")
keep(24, "single continuous rhetorical thought, indivisible")
keep(25, "single clause, indivisible")
keep(26, "single clause, indivisible")
keep(27, "single clause, indivisible")
keep(28, "single clause, indivisible")
keep(29, "single clause, indivisible")
keep(30, "single clause, indivisible")
keep(31, "single clause, indivisible")
keep(32, "single clause, indivisible")
keep(33, "single clause, indivisible")
keep(34, "entire block is the source-attribution lead-in ending ...ལས།, correctly isolated already")
keep(35, "single conditional clause, indivisible")
keep(36, "single continuous clause with citation, indivisible")
keep(37, "single clause, indivisible")
keep(38, "single simile-setup clause, indivisible")
keep(39, "single clause, indivisible")
keep(40, "single clause, indivisible")
keep(41, "single clause, indivisible")
keep(42, "single clause, indivisible")
split_after(43, ["འཇོམས་པར་བྱེད་པའི་སྡུག་བསྔལ་དག་ལ་སྐྲག་དགོས་པའི་གང་ཟག་དག་ནི་"],
            "shift from vivid hell-suffering description to the rhetorical question about guarding the wound")
keep(44, "single clause, indivisible")
keep(45, "single imperative clause, indivisible")
keep(46, "single simile clause, indivisible")
keep(47, "single clause, indivisible")
keep(48, "single simile clause, indivisible")
keep(49, "single clause, indivisible")
keep(50, "single simile clause, indivisible")
keep(51, "single clause, indivisible")
keep(52, "single clause, indivisible")
keep(53, "single clause, indivisible")
keep(54, "single clause, indivisible")
keep(55, "single clause, indivisible")
keep(56, "single clause, indivisible")
keep(57, "single example clause, indivisible")
keep(58, "single clause, indivisible")
keep(59, "single clause, indivisible")
keep(60, "single clause, indivisible")
keep(61, "single clause, indivisible")
keep(62, "single clause, indivisible")
keep(63, "single clause, indivisible")
keep(64, "single imperative clause, indivisible")
keep(65, "single clause, indivisible")
keep(66, "single continuous clause, indivisible")
keep(67, "single clause, indivisible")
keep(68, "single vivid scenario clause, indivisible")

assert len(decisions) == 69, f"expected 69 decisions, got {len(decisions)}"

out = []
for i, d in enumerate(data):
    markers, reason = decisions[i]
    text = d['text']
    new_text = text
    if not markers:
        action = "keep"
    else:
        offset = 0
        for m in markers:
            idx = new_text.find(m, offset)
            if idx == -1:
                raise ValueError(f"marker not found for row {i} idx={d['tsv_idx']}: {m}")
            insert_at = idx + len(m)
            new_text = new_text[:insert_at] + "\n\n" + new_text[insert_at:]
            offset = insert_at + 2
        action = "split"
    out.append({
        "tsv_idx": d["tsv_idx"],
        "block_idx": d["block_idx"],
        "action": action,
        "original": text,
        "new": new_text,
        "reason": reason
    })

fail = []
for row in out:
    a = re.sub(r'\s+', '', row['original'])
    b = re.sub(r'\s+', '', row['new'])
    if a != b:
        fail.append(row['tsv_idx'])

print("verification fails:", fail)
print("split count:", sum(1 for r in out if r['action'] == 'split'))
print("keep count:", sum(1 for r in out if r['action'] == 'keep'))

if fail:
    raise SystemExit("Verification failed, aborting write")

with open('0-INBOX/.stage2-scratch/decisions_03.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("written ok")
