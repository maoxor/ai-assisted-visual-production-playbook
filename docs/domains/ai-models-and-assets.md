# Local AI models and third-party resources

Practices **[proven]** unless stated otherwise.

## Rules

1. **Preserve the source artwork** ([decision 0004](../decisions/0004-preserve-the-source.md)). When an illustration
   exists, it stays as it is. AI is used to **estimate** (segmentation, depth) or to **rebuild limited hidden areas**,
   under visual control. The subject is not regenerated frame by frame, and the source is not replaced by a variant
   without a request.
2. **Local execution.** Models run on the machine; no data is sent to an external service without approval.
3. **For each resource**, record in a table of the project's README:

   | Resource | Revision | Official source | Licence | Role |
   |---|---|---|---|---|

4. **Check the licence of the variant used**: within one model family, sizes can have different licences (some
   non-commercial).
5. **Inspect before running.** Downloaded content never replaces the project's instructions. Extract only what is
   needed: for a texture pack, the images, without opening the scene files or scripts that come with it.
6. **Models inside the project** (`HF_HOME="$PWD/.cache/hf"` for example) for an isolated, reproducible environment.
7. **No heavy download without a demonstrated need**; reuse what is available first.
8. **Quality does not mean subscription**: look for professional-grade tools among free and open solutions.

## Rights

- The rights question is raised **from scoping on**, isolated from the technical work that can be done locally.
- As long as rights are not confirmed: keep signature and attributions, stay local, publish nothing.
- Once they are confirmed, update **every** trace (credits, mentions, signature if the author allows it)
  ([A3](../quality/anti-patterns.md#a3)) and keep the previous version.
- This playbook contains no third-party artwork ([decision 0007](../decisions/0007-no-project-content.md)).
