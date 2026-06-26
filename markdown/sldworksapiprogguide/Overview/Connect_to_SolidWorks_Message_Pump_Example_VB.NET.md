---
title: "Connect to SOLIDWORKS Message Pump (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapiprogguide/Overview/Connect_to_SolidWorks_Message_Pump_Example_VB.NET.htm"
---

# Connect to SOLIDWORKS Message Pump (VB.NET)

## Connect to SOLIDWORKS Message Pump to Handle Keystrokes and Accelerator
Keys (VB.NET)

This example shows how to connect to a SOLIDWORKS message pump by creating,
installing, and uninstalling a hook for a modeless dialog box or PropertyManager
page for intercepting keystrokes and handling accelerator keys.

```vb
' Create, install, and uninstall a hook for a modeless dialog box
' or PropertyManager page for intercepting keystrokes and
' handling accelerator keys
Imports System
Imports System.Runtime.InteropServices
Namespace WinHooks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Class HookEventArgs
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Inherits EventArgs
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public HookCode As Integer kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}' Hook code
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public wParam As IntPtr kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}' WPARAM argument
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public lParam As IntPtr kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}' LPARAM argument
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Class
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Hook Types kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Enum HookType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_JOURNALRECORD = 0
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_JOURNALPLAYBACK = 1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_KEYBOARD = 2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_GETMESSAGE = 3
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_CALLWNDPROC = 4
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_CBT = 5
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_SYSMSGFILTER = 6
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_MOUSE = 7
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_HARDWARE = 8
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_DEBUG = 9
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_SHELL = 10
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_FOREGROUNDIDLE = 11
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_CALLWNDPROCRET = 12
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_KEYBOARD_LL = 13
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}WH_MOUSE_LL = 14
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Enum
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Class LocalWindowsHook
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Filter function delegate
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Delegate Function HookProc(ByVal code As Integer, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Internal properties
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Protected m_hhook As IntPtr = IntPtr.Zero
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Protected m_filterFunc As HookProc = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Protected m_hookType As HookType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Event delegate
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Delegate Sub HookEventHandler(ByVal sender As Object, ByVal e As HookEventArgs)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Event: HookInvoked
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Event HookInvoked As HookEventHandler
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Protected Sub OnHookInvoked(ByVal e As HookEventArgs)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}RaiseEvent HookInvoked(Me, e)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Class constructor(s)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Sub New(ByVal hook As HookType)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_hookType = hook
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_filterFunc = New HookProc(AddressOf Me.CoreHookProc)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Sub New(ByVal hook As HookType, ByVal func As HookProc)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_hookType = hook
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_filterFunc = func
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Default filter function
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Function CoreHookProc(ByVal code As Integer, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Integer
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If code < 0 Then Return CallNextHookEx(m_hhook, code, wParam, lParam)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Let clients determine what to do
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim e As HookEventArgs = New HookEventArgs()
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}e.HookCode = code
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}e.wParam = wParam
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}e.lParam = lParam
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}OnHookInvoked(e)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Yield to the next hook in the chain
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CoreHookProc = CallNextHookEx(m_hhook, code, wParam, lParam)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Function
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Install the hook
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Sub Install()
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}m_hhook = SetWindowsHookEx(m_hookType, m_filterFunc, IntPtr.Zero, AppDomain.GetCurrentThreadId())
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Uninstall the hook
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Public Sub Uninstall()
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}UnhookWindowsHookEx(m_hhook)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Win32 Imports
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Win32: SetWindowsHookEx()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Declare Function SetWindowsHookEx Lib "user32" Alias "SetWindowsHookExA" (ByVal code As HookType, ByVal func As HookProc, ByVal hInstance As IntPtr, ByVal threadID As Integer) As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Win32: UnhookWindowsHookEx()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Declare Function UnhookWindowsHookEx Lib "user32" (ByVal hhook As IntPtr) As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Win32: CallNextHookEx()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Declare Function CallNextHookEx Lib "user32" (ByVal hhook As IntPtr, ByVal code As Integer, ByVal wParam As IntPtr, ByVal lParam As IntPtr) As Integer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Class
End Namespace
```
