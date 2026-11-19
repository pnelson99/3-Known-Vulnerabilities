import hashlib
import os
import pickle
import random
import sqlite3
import subprocess
import tempfile
import yaml


# 1. Arbitrary code execution via eval()
def run_math_expr(user_expr: str):
    return eval(user_expr)


# 2. Arbitrary code execution via exec()
def run_dynamic_snippet(code_str: str, ctx: dict):
    exec(code_str, ctx)
    return ctx


# 3. Hardcoded API token
STRIPE_SECRET_KEY = "sk_live_51NexampleHardcodedSecretToken9999999999"