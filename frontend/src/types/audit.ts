export interface Homepage {
  title: string;

  hero_heading: string;

  hero_subheading: string;

  hero_cta: string;

  announcement_bar: boolean;

  search_present: boolean;

  account_present: boolean;

  wishlist_present: boolean;

  cart_present: boolean;

  navigation_links: string[];

  featured_collections: string[];

  trust_signals: string[];

  newsletter_present: boolean;

  footer_present: boolean;
}

export interface Product {
  url: string;

  title: string;

  currency: string | null;

  price: number | null;

  compare_at_price: number | null;

  discount_percent: number | null;

  rating: number | null;

  review_count: number | null;

  add_to_cart_present: boolean;

  sticky_add_to_cart: boolean;

  shipping_information: boolean;

  returns_information: boolean;

  size_guide_present: boolean;

  breadcrumbs_present: boolean;

  image_count: number;

  variants: string[];

  trust_badges: string[];
}

export interface Recommendation {
  title: string;

  category: string;

  evidence: string;

  impact: number;

  confidence: number;

  effort: number;

  recommendation: string;

  experiment: {
    hypothesis: string;

    primary_metric: string;

    duration: string;
  };
}

export interface Screenshots {
  homepage: string;

  products: string[];
}

export interface AuditResponse {
  homepage: Homepage;

  products: Product[];

  audit: {
    score: number;

    strengths: string[];

    opportunities: Recommendation[];
  };

  screenshots: Screenshots;
  
  report : string;
}