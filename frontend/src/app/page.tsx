import { SearchBar } from "@/components/SearchBar";
import { AuditCardGrid } from "@/components/AuditCardGrid";

export default function HomePage() {
  return (
    <main className="max-w-5xl mx-auto p-6 space-y-8">
      <div className="space-y-2">
        <h1 className="text-2xl font-semibold">SiteSage</h1>
        <p className="text-sm text-muted-foreground">
          Analyze websites for SEO and performance insights.
        </p>
      </div>

      <SearchBar />

      <section className="space-y-4">
        <h2 className="text-lg font-medium">Recent Audits</h2>
        <AuditCardGrid />
      </section>
    </main>
  );
}
