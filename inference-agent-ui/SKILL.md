---
name: inference-agent-ui
description: Build agent chat interfaces with ui.inference.sh in React or Next.js projects using shadcn registry components (Agent, Thread, PromptInput, Response, Tool, and widgets). Use for tasks involving AI chat UX implementation, tool-driven widget rendering, Vercel AI SDK stream protocol wiring, or inference.sh runtime uiTransform integration.
---

# Inference Agent UI

Build production-ready agent interfaces using the `ui.inference.sh` component registry and the AI SDK stream protocol.

Treat this skill as integration guidance, not a design system. Reuse existing app design tokens/layout unless the user asks for a visual redesign.

## Use This Workflow

1. Confirm the integration mode:
- `generic-stream`: Use any backend that returns AI SDK UI message streams.
- `inference-runtime`: Use inference.sh runtime and add `uiTransform`.

2. Install registry components with shadcn:
- Add core primitives first:
  - `npx shadcn@latest add "https://ui.inference.sh/r/agent.json"`
- Add widgets only when needed:
  - `npx shadcn@latest add "https://ui.inference.sh/r/widgets.json"`
- Add optional extras only if the task requires them:
  - `actions.json`, `citations.json`, `sources.json`

3. Wire the backend stream contract:
- Return a UI message stream response compatible with AI SDK.
- If route code uses `streamText`, return `result.toUIMessageStreamResponse()`.
- Keep tool payloads structured and deterministic (stable object shape and typed arguments).

4. Build the client composition in this order:
- Wrap chat surface with `<Agent>`.
- Use `<Thread>` to render message list.
- Render assistant output with `<Response>`.
- Use `<PromptInput>` for input and submit.
- Render tool states with `<Tool>` and map structured tool results to widget components.

5. Add tool + widget behavior:
- Prefer server tools for model-executed actions (search, fetch, DB operations).
- Use client tools only for browser-side side effects (clipboard, local download, navigation).
- Define tool schema clearly so model output maps cleanly to UI widgets.

6. Validate behavior:
- Stream updates appear incrementally in UI (no full-buffer waits).
- Tool calls render loading, success, and error states.
- Invalid tool payloads fail safely and show actionable fallback text.
- Mobile layout remains usable with long responses and many widgets.

## Inference Runtime Mode

Use this mode only when the project is already using inference runtime APIs.

- Keep normal model/tool setup and add:
  - `experimental_transform: [uiTransform({ ... })]`
- Use `uiTransform` to let the model emit UI widget artifacts that map into the provided components.

## Output Contract

When finishing a task, return:

- The chosen mode: `generic-stream` or `inference-runtime`.
- Installed registry bundles and the exact commands used.
- Files changed for backend route, client chat surface, and tool/widget rendering.
- Known limitations, fallback behavior, and any remaining integration risk.

## References

- Capability map and constraints:
  - `references/capability-map.md`
- Starter snippets for API route and chat UI:
  - `references/starter-snippets.md`

Load only the reference file needed for the current task.
