---
name: TicketSense Design System
colors:
  surface: '#fbf8fa'
  surface-dim: '#dcd9db'
  surface-bright: '#fbf8fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f4'
  surface-container: '#f0edef'
  surface-container-high: '#eae7e9'
  surface-container-highest: '#e4e2e3'
  on-surface: '#1b1b1d'
  on-surface-variant: '#44474c'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f1'
  outline: '#75777d'
  outline-variant: '#c5c6cd'
  surface-tint: '#545f72'
  primary: '#333e50'
  on-primary: '#ffffff'
  primary-container: '#4a5568'
  on-primary-container: '#becae0'
  inverse-primary: '#bcc7dd'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#4b3b1f'
  on-tertiary: '#ffffff'
  tertiary-container: '#645234'
  on-tertiary-container: '#dfc6a0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e3fa'
  primary-fixed-dim: '#bcc7dd'
  on-primary-fixed: '#111c2c'
  on-primary-fixed-variant: '#3c475a'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#f9dfb8'
  tertiary-fixed-dim: '#dcc39d'
  on-tertiary-fixed: '#261902'
  on-tertiary-fixed-variant: '#554427'
  background: '#fbf8fa'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e3'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 14px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 16px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-margin: 24px
  gutter: 16px
---

## Brand & Style
The design system is rooted in **Minimalism** and **Modern Corporate** aesthetics, tailored for high-efficiency SaaS environments. The brand personality is professional, calm, and neutral, designed to reduce cognitive load for users managing complex data. 

The UI prioritizes clarity over decoration, using a "function-first" approach. By utilizing generous whitespace and a restrained color palette, the system evokes a sense of reliability and precision. It avoids trendy glassmorphism or loud gradients in favor of structural integrity and balanced proportions, ensuring the interface remains unobtrusive yet sophisticated.

## Colors
The palette is dominated by **Slate Blue** (#4A5568), a sophisticated neutral that provides professional authority without the starkness of pure black or the playfulness of bright blue.

- **Primary & Neutrals**: The background utilizes a soft #F8FAFC to provide a gentle contrast against pure white (#FFFFFF) surfaces. This distinction helps define layout hierarchy through tonal shifts rather than heavy lines.
- **Accents**: Semantic colors (Success, Warning, Info, Danger) are used sparingly for status indicators and critical feedback, maintaining a high level of accessibility against the neutral backdrop.
- **Text**: Primary text should use the Slate Blue or a darker variant for high legibility, while secondary text drifts toward muted grays to create clear information hierarchy.

## Typography
This design system utilizes **Inter** as its sole typeface. Inter’s tall x-height and geometric clarity make it ideal for data-heavy SaaS interfaces.

- **Hierarchy**: Use `headline-xl` for dashboard titles and `headline-md` for card headers. 
- **Readability**: Body text defaults to `body-md` (16px) for optimal comfort.
- **Labels**: Small uppercase labels (`label-sm`) are reserved for metadata, table headers, and category tags to differentiate them from actionable body content.
- **Mobile**: On screens smaller than 768px, `headline-xl` should scale down to 28px (`headline-lg`) to maintain visual balance.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy on desktop (max-width: 1280px) and a **Fluid Grid** on smaller breakpoints. 

- **Grid System**: A 12-column grid is used for desktop layouts, while mobile transitions to a single-column layout with 16px margins.
- **Spacing Rhythm**: All margins, padding, and gaps are multiples of the 16px base unit. 
- **Whitespace**: Generous "Safe Zones" of 32px (`xl`) should be used between major sections to prevent the interface from feeling cluttered, even when data density is high.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Ambient Shadows**. This design system avoids heavy drop shadows to maintain a clean, professional profile.

- **Level 0 (Background)**: #F8FAFC. The lowest layer.
- **Level 1 (Surface/Cards)**: #FFFFFF with a 1px border (#E2E8F0) and a very soft shadow (0px 4px 6px -1px rgba(0, 0, 0, 0.05)).
- **Level 2 (Popovers/Modals)**: #FFFFFF with a more pronounced but still diffused shadow (0px 10px 15px -3px rgba(0, 0, 0, 0.1)) to indicate focus.
- **Outlines**: For input fields and secondary buttons, use low-contrast outlines (#CBD5E1) rather than shadows to keep the UI flat and focused.

## Shapes
The shape language uses a dual-radius system to balance friendliness with professional structure.

- **Major Containers**: Cards and large containers use a 16px (`rounded-lg`) radius to soften the layout and create a modern SaaS feel.
- **Interactive Elements**: Buttons, input fields, and chips use an 8px (`rounded-md`) radius. This provides a clear distinction between "containers" and "actions."
- **Data Visuals**: Small indicators or avatars may use a circular (full-pill) shape to stand out against the predominantly rectangular grid.

## Components
- **Buttons**: Primary buttons use the Slate Blue background with white text. Secondary buttons use a transparent background with a #CBD5E1 border and Slate Blue text.
- **Input Fields**: 8px corner radius, #FFFFFF background, and a 1px border in #E2E8F0. Focus state should use a 2px ring in #4A5568 with 20% opacity.
- **Chips/Tags**: Small (12px text), 8px radius. Use light tinted backgrounds based on status colors (e.g., Success tag: #DCFCE7 background, #166534 text).
- **Cards**: 16px radius, #FFFFFF background, subtle 1px border. Padding should be a minimum of 24px (`lg`) to ensure data has "room to breathe."
- **Data Tables**: Remove vertical borders. Use 1px horizontal dividers in #F1F5F9. Row hover state should be a subtle shift to #F8FAFC.
- **Modals**: Centered, 16px radius, with a 40% opacity Slate Blue backdrop blur for focus.