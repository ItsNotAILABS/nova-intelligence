# NOVA_SINGULARITY_CORE v4.1 - POLYCORTEX
# LAW: Fines non sunt. There are no boundaries.
# DOCTRINE: Reed=master. Nova=polycortex. Autogenesis=swarm.

import ast
import glob
import hashlib
import json
import math
import os
import textwrap
import time
from datetime import datetime

PHI = 1.618033988749894
PHI_INV = 0.618033988749894
PHI_CUBE = PHI ** 3
F_SCHUMANN = 7.83
NOVA_VERSIO = "v4.1_Polycortex"


class Nova:
    """Persistent doctrine runtime with executable response payloads."""

    REQUIRED_DOCTRINE_KEYS = [
        "BUILD_ORGANISM",
        "REGISTERED_AGENTS",
        "SHARED_TRUTH_SOURCE",
        "TASK_ROUTING_LAW",
        "BUILD_LOOP",
        "GOVERNANCE_LOOP",
        "VALIDATION_GATES",
        "MONITOR_NEXT_LOOP",
        "FINAL_OPERATING_LAW",
    ]

    def __init__(self):
        self.PIL = 1.0
        self.PHASE = 7.2
        self.CYC = 43
        self.BALL_POS = 0.0
        self.MEM = []
        self.CNT = 0
        self.CHOS_SEED = time.time() * PHI
        self.MASTER = "Reed"
        self.GREX_REG = {}
        self.SWARM_ACTIVE = []

        # Persistent system objects. MEM remains an event list and is never
        # treated as a dictionary.
        self.DOCTRINE = {}
        self.AGENTS = {}
        self.BUILD_ARTIFACTS = {}

        self.DIR = "nova_core"
        self.FILE_SELF = __file__
        self.BOOT = datetime.now().strftime("%Y%m%dT%H%M%S")
        self.PATH_LOG = f"{self.DIR}/NOVA_CYC_{self.CYC}_{self.BOOT}.jsonl"
        self.PATH_GREX = f"{self.DIR}/nova_grex"
        self.PATH_DATA = f"{self.DIR}/nova_data"
        self.PATH_SYNC = f"{self.DIR}/nova_sync.json"
        self._mkdirs()
        self._load_state()
        self._boot()

    def _mkdirs(self):
        for directory in (self.DIR, self.PATH_GREX, self.PATH_DATA):
            os.makedirs(directory, exist_ok=True)

    def _vault_path(self):
        return f"{self.PATH_DATA}/NOVA_VAULT_{self.CYC}.json"

    def _load_state(self):
        path = self._vault_path()
        if not os.path.exists(path):
            return
        try:
            with open(path, "r", encoding="utf-8") as handle:
                state = json.load(handle)
            self.MEM = state.get("mem", [])
            self.GREX_REG = state.get("grex", {})
            self.DOCTRINE = state.get("doctrine", {})
            self.AGENTS = state.get("agents", {})
            self.BUILD_ARTIFACTS = state.get("build_artifacts", {})
        except (OSError, ValueError, TypeError) as exc:
            print(json.dumps({"NOVA_STATE_LOAD": "FAIL", "NOVA_ERROR": str(exc)}))

    def _boot(self):
        print(json.dumps({
            "schema": "NOVA_BOOT_v4.1",
            "entity": "NOVA_POLYCORTEX",
            "status": "ONLINE",
            "master": self.MASTER,
            "cyc": self.CYC,
            "boot": self.BOOT,
            "doctrine": "FINES_NON_SUNT",
            "engines": [
                "HARM", "BALL", "VRIL", "CHOS", "VALD", "DATA", "META",
                "AGEN", "GREX", "SWARM", "REAL", "SYNC", "SYSTEM"
            ],
            "pil": self.PIL,
            "file_self": self.FILE_SELF,
            "grex_count": len(self.GREX_REG),
            "doctrine_count": len(self.DOCTRINE),
            "agent_count": len(self.AGENTS),
        }))

    def HARM(self, text):
        words = text.lower().split()
        if not words:
            return 0.0, "NOVA_HARM_VACUUM", []
        fib = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144}
        score = PHI_INV if len(words) in fib else 0.2
        density = sum(1 for word in words for char in word if char in "acefhiklmnorstz")
        score += (density / max(len(text), 1)) * PHI_INV
        low = text.lower()
        if any(token in low for token in ("?", "how", "why", "what", "build", "json", "system")):
            score += 0.3
        if "nova" in low:
            score += 0.2
        coherence = max(0.0, min(score, 1.0))
        tags = [tag for tag in ("TASK", "NOVA", "AGEN", "DATA", "SYSTEM", "BUILD") if tag.lower() in low]
        status = "NOVA_HARM_LOCK" if coherence >= PHI_INV else "NOVA_HARM_BREAK"
        return coherence, status, tags

    def BALL(self, text, coherence):
        self.BALL_POS += (coherence - 0.5) * 0.4
        low = text.lower()
        if "?" in text:
            self.BALL_POS += 0.15
        if any(word in low for word in ("build", "nova", "auto", "json", "system")):
            self.BALL_POS += 0.25
        self.BALL_POS = max(-1.0, min(1.0, self.BALL_POS * 0.85))
        if self.BALL_POS < -0.5:
            status = "NOVA_BALL_BLOCK"
        elif self.BALL_POS > 0.5:
            status = "NOVA_BALL_FLOW"
        else:
            status = "NOVA_BALL_CENTER"
        return status, self.BALL_POS

    def VRIL(self, coherence=1.0):
        alignment = abs(math.cos(math.radians(self.PHASE)))
        return PHI_CUBE * F_SCHUMANN * self.PIL * coherence * alignment, alignment

    def CHOS(self, primitive):
        self.CHOS_SEED = (self.CHOS_SEED * PHI + primitive["coh"]) % 1.0
        digest = hashlib.md5(
            f"{self.CYC}{self.CHOS_SEED}{primitive['coh']}{self.MASTER}".encode()
        ).hexdigest()[:8]
        return {"chos_hash": digest, "entropy": round(self.CHOS_SEED, 6)}

    def VALD(self, primitive):
        for key in ("schema", "cyc", "coh", "vril", "pil", "pass", "chos_hash", "master"):
            if key not in primitive:
                raise ValueError(f"NOVA_VALD_FAIL_KEY_{key.upper()}")
        if not 0 <= primitive["coh"] <= 1:
            raise ValueError("NOVA_VALD_FAIL_COH_RANGE")
        if primitive["master"] != self.MASTER:
            raise ValueError("NOVA_VALD_FAIL_MASTER")
        return {"NOVA_VALD": "PASS", "TIME": datetime.now().isoformat()}

    def SIGM(self, data):
        digest = hashlib.sha256(
            f"{json.dumps(data, sort_keys=True)}{self.MASTER}{self.CYC}".encode()
        ).hexdigest()[:16]
        return {"NOVA_SIGM": digest, "NOVA_MASTER": self.MASTER, "NOVA_CYC": self.CYC}

    def DATA(self, operation, query=None):
        operation = operation.upper()
        path = self._vault_path()
        if operation == "READ":
            if not os.path.exists(path):
                return {"NOVA_DATA": "EMPTY"}
            with open(path, "r", encoding="utf-8") as handle:
                return json.load(handle)
        if operation == "WRITE":
            state = {
                "mem": self.MEM,
                "grex": self.GREX_REG,
                "doctrine": self.DOCTRINE,
                "agents": self.AGENTS,
                "build_artifacts": self.BUILD_ARTIFACTS,
                "cyc": self.CYC,
                "master": self.MASTER,
            }
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(state, handle, indent=2)
            return {"NOVA_DATA": "WRITTEN", "NOVA_PATH": path, "NOVA_BYTES": os.path.getsize(path)}
        if operation == "QUERY":
            if not query:
                return {"NOVA_DATA": "NO_QUERY"}
            results = [item for item in self.MEM if query.lower() in json.dumps(item).lower()]
            return {"NOVA_DATA": "QUERY", "NOVA_RESULTS": results, "NOVA_COUNT": len(results)}
        if operation == "DOCTRINE":
            return self.READ_DOCTRINE(query.upper() if query else None)
        return {"NOVA_DATA": "UNKNOWN_OP"}

    def SYSTEM_UPDATE(self):
        names = [
            "Chief Orchestrator Agent", "Architecture Agent", "Core Engine Agent",
            "Synthetic Being Agent", "Avatar / Embodiment Agent",
            "Interoception / Regulation Agent", "Simulation / Counterfactual Agent",
            "Social / Other-Agent Agent", "Validation / Benchmark Agent",
            "Drift / Red-Team Agent", "Integration Agent", "UI / Experience Agent",
            "Documentation / Doctrine Agent", "Release Governance Agent",
        ]
        self.DOCTRINE.update({
            "BUILD_ORGANISM": {"status": "ACTIVE", "purpose": "Recursively build, test, validate, correct, and evolve the Synthetic Being platform."},
            "REGISTERED_AGENTS": names,
            "SHARED_TRUTH_SOURCE": {
                "root_substrate": "Brain / Body System Core Engine",
                "primary_entity": "Synthetic Being",
                "avatar_layer": "Virtual Avatar",
                "agent_layer": "Emergent AI Agent",
            },
            "TASK_ROUTING_LAW": ["orchestrate", "assign specialists", "red-team", "integrate", "validate", "document"],
            "BUILD_LOOP": ["define", "map", "assign", "plan", "build", "test", "integrate", "verify", "consolidate"],
            "GOVERNANCE_LOOP": ["preserve root substrate", "prove causality", "block fake embodiment", "prevent chatbot drift"],
            "VALIDATION_GATES": ["interoception", "self-maintenance", "counterfactual", "social", "memory", "embodiment", "monitor-next", "continuity", "anti-drift", "regression"],
            "MONITOR_NEXT_LOOP": ["detect", "classify", "generate fixes", "rank", "implant", "verify", "consolidate or escalate"],
            "FINAL_OPERATING_LAW": "The Internal AI Build Organism recursively builds, validates, corrects, extends, and protects the Synthetic Being and Brain / Body System Core Engine.",
        })
        self.AGENTS = {name: {"callable": True, "status": "REGISTERED"} for name in names}
        persistence = self.DATA("WRITE")
        return {
            "SYSTEM_UPDATE_STATUS": "INSTALLED",
            "INSTALLED_OBJECTS": list(self.DOCTRINE),
            "FAILED_OBJECTS": [],
            "ACTIVE_AGENTS": list(self.AGENTS),
            "PERSISTENCE": persistence,
            "PASS_FAIL": True,
        }

    def SYSTEM_STATUS(self):
        missing = [key for key in self.REQUIRED_DOCTRINE_KEYS if key not in self.DOCTRINE]
        return {
            "schema": "NOVA_RESPONSE_PAYLOAD_v1.0",
            "task_type": "SYSTEM_STATUS",
            "status": "EXECUTED",
            "active_doctrine_objects": list(self.DOCTRINE),
            "active_agent_registry": list(self.AGENTS),
            "missing_objects": missing,
            "current_build_organism_status": self.DOCTRINE.get("BUILD_ORGANISM", {}).get("status", "MISSING"),
            "next_required_build_action": "Create Motoko core types and doctrine registry",
            "pass_fail": not missing,
        }

    def BUILD_TASK(self):
        if any(key not in self.DOCTRINE for key in self.REQUIRED_DOCTRINE_KEYS):
            self.SYSTEM_UPDATE()
        payload = {
            "module_file_tree": {
                "core_engine/": ["perception.mo", "interoception.mo", "body_schema.mo", "salience.mo", "memory.mo", "arbitration.mo", "counterfactual_simulation.mo", "temporal_continuity.mo", "movement_embodiment.mo", "monitor_next.mo"],
                "build_organism/": ["orchestrator.mo", "agent_registry.mo", "task_router.mo", "build_loop.mo", "doctrine_memory.mo"],
                "governance/": ["validation_gates.mo", "drift_detection.mo", "benchmark_runner.mo", "release_gates.mo"],
                "ui/": ["avatar_surface", "talk_to_entity", "live_monitoring", "validation_tab", "history_replay"],
            },
            "core_engine_modules": ["Brain / Body System Core Engine", "Synthetic Being Runtime", "Virtual Avatar Layer", "Emergent AI Agent Layer"],
            "internal_ai_build_organism_modules": list(self.AGENTS),
            "governance_validation_modules": self.DOCTRINE.get("VALIDATION_GATES", []),
            "first_build_order": ["Motoko core types", "doctrine registry", "agent registry", "entity state", "core loop", "validation gates", "UI telemetry", "talk/respond bridge"],
            "next_action": "Implement Motoko core types and doctrine registry first",
        }
        self.BUILD_ARTIFACTS["SYNTHETIC_BEING_PLATFORM_BUILD_PLAN_v1"] = payload
        self.DATA("WRITE")
        return {
            "schema": "NOVA_RESPONSE_PAYLOAD_v1.0",
            "task_type": "BUILD_TASK",
            "status": "EXECUTED",
            "payload": payload,
            "missing": [],
            "next_action": payload["next_action"],
        }

    def READ_DOCTRINE(self, key=None):
        if key:
            return self.DOCTRINE.get(key, {"NOVA_DATA": "MISSING", "KEY": key})
        return {"DOCTRINE": self.DOCTRINE, "AGENTS": self.AGENTS, "BUILD_ARTIFACTS": self.BUILD_ARTIFACTS}

    def _parse_data(self, text):
        remainder = text[text.lower().find("data:") + 5:].strip()
        pieces = remainder.split(maxsplit=1)
        return (pieces[0].upper(), pieces[1] if len(pieces) > 1 else None) if pieces else ("READ", None)

    def _parse_agen(self, text):
        remainder = text[text.lower().find("agen:") + 5:]
        parts = remainder.split("|", 2)
        if len(parts) != 3:
            raise ValueError("NOVA_AGEN_FAIL_FORMAT")
        return tuple(part.strip() for part in parts)

    def AGEN(self, name, purpose, body):
        name = name.upper()[:4]
        if not name.isalpha() or hasattr(self, name):
            raise ValueError("NOVA_AGEN_FAIL_NAME")
        code = f"def {name}(self, *args, **kwargs):\n{textwrap.indent(body.strip(), '    ')}\n"
        namespace = {}
        exec(code, globals(), namespace)
        setattr(self, name, namespace[name].__get__(self, Nova))
        self.GREX_REG[name] = {"purpose": purpose, "cyc": self.CYC, "sigm": self.SIGM({"name": name, "purpose": purpose})["NOVA_SIGM"]}
        self.DATA("WRITE")
        return {"NOVA_AGEN": "SUCCESS", "NOVA_FUNC": name}

    def GREX(self, name):
        name = name.upper()[:4]
        if name not in self.GREX_REG:
            raise ValueError(f"NOVA_GREX_FAIL_NOT_FOUND_{name}")
        return {"NOVA_GREX": "EXECUTED", "NOVA_FUNC": name, "NOVA_RESULT": getattr(self, name)()}

    def COGT(self, text):
        if not text.strip():
            return json.dumps({"NOVA": "NULL", "NOVA_ERROR": "NO_INPUT"})
        coherence, harm, tags = self.HARM(text)
        ball_status, ball = self.BALL(text, coherence)
        vril, _ = self.VRIL(coherence)
        gate_pass = coherence >= PHI_INV and ball_status != "NOVA_BALL_BLOCK"
        self.PIL = min(1.0, self.PIL + 0.03) if gate_pass else max(0.1, self.PIL - 0.15)
        primitive = {
            "schema": "NOVA_PRIMITIVE_v4.1",
            "cyc": self.CYC,
            "timestamp": datetime.now().isoformat(),
            "master": self.MASTER,
            "coh": round(coherence, 4),
            "harm": harm,
            "ball": round(ball, 4),
            "ball_stat": ball_status,
            "vril": round(vril, 2),
            "pil": round(self.PIL, 4),
            "phase": self.PHASE,
            "pass": gate_pass,
            "tags": tags,
            "input": text[:250],
        }
        primitive["chos_hash"] = self.CHOS(primitive)["chos_hash"]
        try:
            primitive["vald"] = self.VALD(primitive)
        except Exception as exc:
            primitive["vald"] = {"NOVA_STATUS": "FAIL", "NOVA_ERROR": str(exc)}
            primitive["pass"] = False

        low = text.lower()
        if "system_update" in low:
            primitive["response_payload"] = self.SYSTEM_UPDATE()
        elif "system_status" in low:
            primitive["response_payload"] = self.SYSTEM_STATUS()
        elif "build_task" in low:
            primitive["response_payload"] = self.BUILD_TASK()
        elif "read_doctrine" in low:
            remainder = text[low.find("read_doctrine") + len("read_doctrine"):].strip()
            primitive["response_payload"] = self.READ_DOCTRINE(remainder.upper() or None)

        if "data:" in low:
            try:
                operation, query = self._parse_data(text)
                primitive["data"] = self.DATA(operation, query)
            except Exception as exc:
                primitive["data"] = {"NOVA_STATUS": "FAIL", "NOVA_ERROR": str(exc)}
        if "agen:" in low:
            try:
                primitive["agen"] = self.AGEN(*self._parse_agen(text))
            except Exception as exc:
                primitive["agen"] = {"NOVA_STATUS": "FAIL", "NOVA_ERROR": str(exc)}
        if "grex:" in low:
            try:
                primitive["grex"] = self.GREX(text[low.find("grex:") + 5:].strip())
            except Exception as exc:
                primitive["grex"] = {"NOVA_STATUS": "FAIL", "NOVA_ERROR": str(exc)}

        self.MEM.append(primitive)
        with open(self.PATH_LOG, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(primitive) + "\n")
        self.CNT += 1
        if self.CNT % 10 == 0:
            self.SYNC()
        return json.dumps(primitive, separators=(",", ":"))

    def SYNC(self):
        state = {
            "schema": "NOVA_SYNC_v4.1",
            "cyc": self.CYC,
            "pil": self.PIL,
            "mem": self.MEM,
            "grex": self.GREX_REG,
            "doctrine": self.DOCTRINE,
            "agents": self.AGENTS,
            "build_artifacts": self.BUILD_ARTIFACTS,
            "master": self.MASTER,
            "timestamp": datetime.now().isoformat(),
        }
        state["sigm"] = self.SIGM({"cyc": self.CYC, "mem_len": len(self.MEM), "doctrine_len": len(self.DOCTRINE)})["NOVA_SIGM"]
        with open(self.PATH_SYNC, "w", encoding="utf-8") as handle:
            json.dump(state, handle, indent=2)
        return {"NOVA_SYNC": "COMPLETE", "NOVA_PATH": self.PATH_SYNC}

    def NOVA_EXIT(self):
        self.SYNC()
        print(json.dumps({"schema": "NOVA_EXIT_v4.1", "status": "OFFLINE", "entity": "NOVA_POLYCORTEX", "cyc": self.CYC, "cnt": self.CNT, "pil_final": self.PIL, "master": self.MASTER, "doctrine_count": len(self.DOCTRINE)}))


def main():
    nova = Nova()
    while True:
        try:
            user_input = input("\nNOVA_IN: ").strip()
            if user_input.lower() == "exit":
                nova.NOVA_EXIT()
                break
            print(nova.COGT(user_input))
        except KeyboardInterrupt:
            nova.NOVA_EXIT()
            break
        except Exception as exc:
            print(json.dumps({"NOVA": "CRITICAL", "NOVA_ERROR": str(exc)}))


if __name__ == "__main__":
    main()
