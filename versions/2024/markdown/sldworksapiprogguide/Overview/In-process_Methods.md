---
title: "In-process Methods"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/In-process_Methods.htm"
---

# In-process Methods

The SOLIDWORKS API provides two types of methods for interfaces that
get or set arrays:

- in-process
- global

In-process methods typically begin with the letter I and get or set
pointers to arrays that only[unmanaged
C++ applications](Unmanaged_CPP_and_CPP_CLI_Code_Differences.htm)can handle. Global methods (i.e.,
similarly named methods that do not begin with the letter I) are useful both inside a process and across processes and return
predictable results for all of the SOLIDWORKS supported languages.

For example,[IView](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView.html)contains:

- [IView::IGetCThreads](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~IGetCThreads.html)(in-process)
- [IView::GetCThreads](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IView~GetCThreads.html)kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}(global)

These methods perform similar work in different languages.

| For... | IView::IGetCThreads gets... | IView::GetCThreads gets... |
| --- | --- | --- |
| VBA, VB.NET, C#, and C++/CLI
(also called managed C++) | a CThread | a VARIANT array of
CThreads |
| Unmanaged
C++ | an array of
CThreads | a pointer to a CThread |

In general:

- For VBA, VB.NET, C#, and C++/CLI (also called managed
  C++), in-process methods get or set a strongly typed object, and global
  methods get or set a VARIANT array.
- For unmanaged C++, in-process methods get or set a pointer
  to an array of Dispatch objects, and global methods get or set a pointer to
  a Dispatch object.

The following unmanaged C++ code example uses the flag, useInProcessMethod,
to switch between the in-process method, IView::IGetCThreads,
and the global method, IView::GetCThreads:

```vb
STDMETHODIMP CCTDemo::ToolbarCallback0(void)
{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CComPtr<IModelDoc2> swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}iSwApp->get_IActiveDoc2(&swModel);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}CComQIPtr<IDrawingDoc> swDraw = swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swDraw)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}CComPtr<IView> viewSheet;
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}swDraw->IGetFirstView(&viewSheet);
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}CComPtr<IView> viewFirst;
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}viewSheet->IGetNextView(&viewFirst);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}if (viewFirst)
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}bool useInProcessMethod = false;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}///Using IGetCThreads
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}if (useInProcessMethod)
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}long count;
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}viewFirst->GetCThreadCount(&count);
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}if (count > 0)
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}CString msg;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}msg.Format(_T("Number of threads: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}%d"), count);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}long res0;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(msg),0,0,&res0);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}ICThread** rawThreadArray = new ICThread*[count];
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}viewFirst->IGetCThreads(count, rawThreadArray);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}CComPtr<INote> threadCalloutNote;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}rawThreadArray[0]->get_ThreadCallout(&threadCalloutNote);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}if (threadCalloutNote)
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}CComBSTR noteText;
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}threadCalloutNote->GetText(¬eText);
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}CComBSTR msg(_T("Cosmetic thread callout text: "));
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}if (noteText != NULL)
kadov_tag{{<spaces>}}                                                kadov_tag{{</spaces>}}msg.Append(noteText);
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}long res1;
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(msg),0,0,&res1);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}//Be sure to release your resources when you are finished.
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}for (int arrayIndex = 0; arrayIndex != count; ++arrayIndex)
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}rawThreadArray[arrayIndex]->Release();
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}delete[] rawThreadArray;
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}long res2;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(_T("No threads in drawing view.")),0,0,&res2);
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}///Using GetCThreads
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}///Note the use of SafeDISPATCHArray. This is a VARIANT helper class
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}///that was defined in a template class.
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}long count;
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}viewFirst->GetCThreadCount(&count);
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}if (count > 0)
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}VARIANT vThreads;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}VariantInit(&vThreads);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}viewFirst->GetCThreads(&vThreads);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}SafeDISPATCHArray variantThreadArray(&vThreads);
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}CComQIPtr<ICThread> swThread = variantThreadArray[0];
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}CComPtr<INote> threadCalloutNote;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}swThread->get_ThreadCallout(&threadCalloutNote);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}if (threadCalloutNote)
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}CComBSTR noteText;
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}threadCalloutNote->GetText(¬eText);
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}CComBSTR msg(_T("Cosmetic thread callout text: "));
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}if (noteText != NULL)
kadov_tag{{<spaces>}}                                                kadov_tag{{</spaces>}}msg.Append(noteText);
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}long res1;
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(msg),0,0,&res1);
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}//Be sure to release your resources when you are finished.
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}for (int arrayIndex = 0; arrayIndex != count; ++arrayIndex)
kadov_tag{{<spaces>}}                                          kadov_tag{{</spaces>}}variantThreadArray[arrayIndex]->Release();
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}long res2;
kadov_tag{{<spaces>}}                                    kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(_T("No threads in drawing view.")),0,0,&res2);
kadov_tag{{<spaces>}}                              kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}long res3;
kadov_tag{{<spaces>}}                        kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(_T("No drawing view.")),0,0,&res3);
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}long res4;
kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}iSwApp->SendMsgToUser2(CComBSTR(_T("No drawing.")),0,0,&res4);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}      kadov_tag{{</spaces>}}return S_OK;
}
```

A VBA programmer might hope that IView::IGetCThreads returns an array. But
this in-process method returns an array only for unmanaged C++. For
VBA, the in-process method returns one strongly typed object, CThread. For
example:

```vb
Dim instance As IView
Dim numCThread As Integer
Dim value As CThread
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
value = instance.IGetCThreads(numCThread)
```

To reliably obtain the complete array of CThreads, a VBA programmer
(or C# or C++/CLI programmer) should always use the global method
(e.g., IView::GetCThreads). For VBA, IView::GetCThreads returns a VARIANT array of CThreads.kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
example:

```vb
Option Explicit
Dim instance As IView
Dim vObj As Variant
Dim CurrCT As SldWorks.Annotation
Dim value As Variant
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
Sub main()
```

```vb
Set swApp = Application.SldWorks
Set swModel = swApp.GetFirstDocument
Set instance = swModel.ActiveView

value = instance.GetCThreads
If Not value Is Nothing Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 to UBound(value)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set CurrCT = value(i)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print CurrCT.GetName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i
End If
```

```vb
End Sub
For more information about using smart pointers with container classes, see STL Container Classes and Smart Pointers.
```
