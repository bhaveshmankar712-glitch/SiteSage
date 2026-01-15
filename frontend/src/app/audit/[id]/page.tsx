"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import { AuditService, AuditDetail } from "@/services/audit.service";
import { AuditDetailView } from "@/components/AuditDetailView";
import { Skeleton } from "@/components/ui/skeleton";

export default function AuditDetailPage() {
  const { id } = useParams<{ id: string }>();
  const [audit, setAudit] = useState<AuditDetail | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    AuditService.getAuditById(id)
      .then(setAudit)
      .catch((err) => setError(err.message));
  }, [id]);

  if (error) {
    return (
      <main className="max-w-4xl mx-auto p-6">
        <p className="text-red-600">{error}</p>
      </main>
    );
  }

  if (!audit) {
    return (
      <main className="max-w-4xl mx-auto p-6 space-y-4">
        <Skeleton className="h-8 w-2/3" />
        <Skeleton className="h-24" />
        <Skeleton className="h-24" />
      </main>
    );
  }

  return (
    <main className="max-w-4xl mx-auto p-6">
      <AuditDetailView audit={audit} />
    </main>
  );
}
