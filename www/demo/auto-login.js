async function haAutoLogin(username, password) {
  const clientId = `${window.location.origin}/`;

  const createResponse = await fetch("/auth/login_flow", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      client_id: clientId,
      handler: ["homeassistant", null],
    }),
  });

  if (!createResponse.ok) {
    throw new Error(`Login flow failed (${createResponse.status})`);
  }

  const createPayload = await createResponse.json();
  const submitResponse = await fetch(`/auth/login_flow/${createPayload.flow_id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  if (!submitResponse.ok) {
    throw new Error(`Login submit failed (${submitResponse.status})`);
  }

  const submitPayload = await submitResponse.json();
  if (submitPayload.type !== "create_entry") {
    throw new Error(submitPayload.errors?.base?.[0] || "Invalid demo credentials");
  }

  return submitPayload;
}

function showFallback(message) {
  const loading = document.getElementById("loading");
  const fallback = document.getElementById("fallback");
  const error = document.getElementById("error");
  if (loading) loading.hidden = true;
  if (fallback) fallback.hidden = false;
  if (error) error.textContent = message;
}

function fillCredentialFields() {
  const auth = window.DEMO_AUTH || {};
  const userField = document.getElementById("username");
  const passField = document.getElementById("password");
  if (userField && auth.username) userField.value = auth.username;
  if (passField && auth.password) passField.value = auth.password;
}

async function startDemoLogin() {
  const auth = window.DEMO_AUTH || {};
  if (!auth.username || !auth.password) {
    showFallback("Set DEMO_USERNAME and DEMO_PASSWORD in Dokploy, then redeploy.");
    fillCredentialFields();
    return;
  }

  try {
    await haAutoLogin(auth.username, auth.password);
    window.location.href = auth.dashboard || "/lovelace/nvision-demo";
  } catch (error) {
    showFallback(error.message || "Auto-login failed.");
    fillCredentialFields();
  }
}

window.addEventListener("DOMContentLoaded", () => {
  fillCredentialFields();
  void startDemoLogin();
});
