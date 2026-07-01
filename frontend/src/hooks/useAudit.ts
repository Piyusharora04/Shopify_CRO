import { useState } from "react";
import api from "../services/api";
import type { AuditResponse }  from "../types/audit";

export function useAudit() {
  const [loading, setLoading] = useState(false);

  const [data, setData] = useState<AuditResponse | null>(null);

  async function analyze(url: string) {
    setLoading(true);

    try {
      const response = await api.post<AuditResponse>(
        "/api/analyze",
        {
          url,
        }
      );

      setData(response.data);
    } finally {
      setLoading(false);
    }
  }

  return {
    loading,
    data,
    analyze,
  };
}