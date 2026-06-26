---
title: "Connect to SOLIDWORKS Message Pump to Handle Keystrokes and Accelerator Keys (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapiprogguide/Overview/Connect_to_SolidWorks_Message_Pump_Example_CSharp.htm"
---

# Connect to SOLIDWORKS Message Pump to Handle Keystrokes and Accelerator Keys (C#)

This example shows how to connect to a SOLIDWORKS message pump by creating,
installing, and uninstalling a hook for a modeless dialog box or PropertyManager
page for intercepting keystrokes and handling accelerator keys.

```vb
//Create, install, and uninstall a hook for a modeless dialog box
//or PropertyManager page for intercepting keystrokes and
//handling accelerator keys
using System;
using System.Runtime.InteropServices;
namespace WinHooks
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public class HookEventArgs : EventArgs
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int HookCode; kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}// Hook code
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public IntPtr wParam; kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}// WPARAM argument
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public IntPtr lParam; kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}// LPARAM argument
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}// Hook Types kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public enum HookType : int
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_JOURNALRECORD = 0,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_JOURNALPLAYBACK = 1,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_KEYBOARD = 2,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_GETMESSAGE = 3,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_CALLWNDPROC = 4,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_CBT = 5,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_SYSMSGFILTER = 6,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_MOUSE = 7,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_HARDWARE = 8,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_DEBUG = 9,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_SHELL = 10,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_FOREGROUNDIDLE = 11,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_CALLWNDPROCRET = 12, kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_KEYBOARD_LL = 13,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_MOUSE_LL = 14
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public class LocalWindowsHook
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Filter function delegate
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public delegate int HookProc(int code, IntPtr wParam,
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}IntPtr lParam);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Internal properties
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected IntPtr m_hhook = IntPtr.Zero;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected HookProc m_filterFunc = null;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected HookType m_hookType;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Event delegate
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public delegate void HookEventHandler(object sender, HookEventArgs e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Event: HookInvoked
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public event HookEventHandler HookInvoked;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected void OnHookInvoked(HookEventArgs e)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (HookInvoked != null)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}HookInvoked(this, e);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Class constructor(s)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public LocalWindowsHook(HookType hook)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_hookType = hook;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_filterFunc = new HookProc(this.CoreHookProc);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public LocalWindowsHook(HookType hook, HookProc func)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_hookType = hook;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_filterFunc = func;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}} kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Default filter function
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int CoreHookProc(int code, IntPtr wParam, IntPtr lParam)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (code < 0)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return CallNextHookEx(m_hhook, code, wParam, lParam);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Let clients determine what to do
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}HookEventArgs e = new HookEventArgs();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}e.HookCode = code;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}e.wParam = wParam;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}e.lParam = lParam;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}OnHookInvoked(e);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Yield to the next hook in the chain
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return CallNextHookEx(m_hhook, code, wParam, lParam);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Install the hook
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Install()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_hhook = SetWindowsHookEx(
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}m_hookType,
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}m_filterFunc,
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}IntPtr.Zero,
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}(int) AppDomain.GetCurrentThreadId());
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Uninstall the hook
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Uninstall()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}UnhookWindowsHookEx(m_hhook);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#region Win32 Imports
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Win32: SetWindowsHookEx()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}[DllImport("user32.dll")]
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected static extern IntPtr SetWindowsHookEx(HookType code,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}HookProc func,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IntPtr hInstance,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int threadID);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Win32: UnhookWindowsHookEx()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}[DllImport("user32.dll")]
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected static extern int UnhookWindowsHookEx(IntPtr hhook);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Win32: CallNextHookEx()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}[DllImport("user32.dll")]
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}protected static extern int CallNextHookEx(IntPtr hhook,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int code, IntPtr wParam, IntPtr lParam);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}#endregion
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
