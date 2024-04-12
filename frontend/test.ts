
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const myCustomTheme: CustomThemeConfig = {
    name: 'test',
    properties: {
		// =~= Theme Properties =~=
		"--theme-font-family-base": `system-ui`,
		"--theme-font-family-heading": `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'`,
		"--theme-font-color-base": "0 0 0",
		"--theme-font-color-dark": "255 255 255",
		"--theme-rounded-base": "24px",
		"--theme-rounded-container": "8px",
		"--theme-border-base": "0px",
		// =~= Theme On-X Colors =~=
		"--on-primary": "255 255 255",
		"--on-secondary": "255 255 255",
		"--on-tertiary": "0 0 0",
		"--on-success": "0 0 0",
		"--on-warning": "0 0 0",
		"--on-error": "255 255 255",
		"--on-surface": "0 0 0",
		// =~= Theme Colors  =~=
		// primary | #000000 
		"--color-primary-50": "217 217 217", // #d9d9d9
		"--color-primary-100": "204 204 204", // #cccccc
		"--color-primary-200": "191 191 191", // #bfbfbf
		"--color-primary-300": "153 153 153", // #999999
		"--color-primary-400": "77 77 77", // #4d4d4d
		"--color-primary-500": "0 0 0", // #000000
		"--color-primary-600": "0 0 0", // #000000
		"--color-primary-700": "0 0 0", // #000000
		"--color-primary-800": "0 0 0", // #000000
		"--color-primary-900": "0 0 0", // #000000
		// secondary | #000000 
		"--color-secondary-50": "217 217 217", // #d9d9d9
		"--color-secondary-100": "204 204 204", // #cccccc
		"--color-secondary-200": "191 191 191", // #bfbfbf
		"--color-secondary-300": "153 153 153", // #999999
		"--color-secondary-400": "77 77 77", // #4d4d4d
		"--color-secondary-500": "0 0 0", // #000000
		"--color-secondary-600": "0 0 0", // #000000
		"--color-secondary-700": "0 0 0", // #000000
		"--color-secondary-800": "0 0 0", // #000000
		"--color-secondary-900": "0 0 0", // #000000
		// tertiary | #0EA5E9 
		"--color-tertiary-50": "219 242 252", // #dbf2fc
		"--color-tertiary-100": "207 237 251", // #cfedfb
		"--color-tertiary-200": "195 233 250", // #c3e9fa
		"--color-tertiary-300": "159 219 246", // #9fdbf6
		"--color-tertiary-400": "86 192 240", // #56c0f0
		"--color-tertiary-500": "14 165 233", // #0EA5E9
		"--color-tertiary-600": "13 149 210", // #0d95d2
		"--color-tertiary-700": "11 124 175", // #0b7caf
		"--color-tertiary-800": "8 99 140", // #08638c
		"--color-tertiary-900": "7 81 114", // #075172
		// success | #84cc16 
		"--color-success-50": "237 247 220", // #edf7dc
		"--color-success-100": "230 245 208", // #e6f5d0
		"--color-success-200": "224 242 197", // #e0f2c5
		"--color-success-300": "206 235 162", // #ceeba2
		"--color-success-400": "169 219 92", // #a9db5c
		"--color-success-500": "132 204 22", // #84cc16
		"--color-success-600": "119 184 20", // #77b814
		"--color-success-700": "99 153 17", // #639911
		"--color-success-800": "79 122 13", // #4f7a0d
		"--color-success-900": "65 100 11", // #41640b
		// warning | #EAB308 
		"--color-warning-50": "252 244 218", // #fcf4da
		"--color-warning-100": "251 240 206", // #fbf0ce
		"--color-warning-200": "250 236 193", // #faecc1
		"--color-warning-300": "247 225 156", // #f7e19c
		"--color-warning-400": "240 202 82", // #f0ca52
		"--color-warning-500": "234 179 8", // #EAB308
		"--color-warning-600": "211 161 7", // #d3a107
		"--color-warning-700": "176 134 6", // #b08606
		"--color-warning-800": "140 107 5", // #8c6b05
		"--color-warning-900": "115 88 4", // #735804
		// error | #B00020 
		"--color-error-50": "243 217 222", // #f3d9de
		"--color-error-100": "239 204 210", // #efccd2
		"--color-error-200": "235 191 199", // #ebbfc7
		"--color-error-300": "223 153 166", // #df99a6
		"--color-error-400": "200 77 99", // #c84d63
		"--color-error-500": "176 0 32", // #B00020
		"--color-error-600": "158 0 29", // #9e001d
		"--color-error-700": "132 0 24", // #840018
		"--color-error-800": "106 0 19", // #6a0013
		"--color-error-900": "86 0 16", // #560010
		// surface | #ffffff 
		"--color-surface-50": "255 255 255", // #ffffff
		"--color-surface-100": "255 255 255", // #ffffff
		"--color-surface-200": "255 255 255", // #ffffff
		"--color-surface-300": "255 255 255", // #ffffff
		"--color-surface-400": "255 255 255", // #ffffff
		"--color-surface-500": "255 255 255", // #ffffff
		"--color-surface-600": "230 230 230", // #e6e6e6
		"--color-surface-700": "191 191 191", // #bfbfbf
		"--color-surface-800": "153 153 153", // #999999
		"--color-surface-900": "125 125 125", // #7d7d7d
		
	}
}