---
title: "SolidWorks.Interop.swbrowser Namespace"
project: "SOLIDWORKS Toolbox Browser API"
interface: "SolidWorks.Interop.swbrowser"
member: ""
kind: "namespace"
source: "toolboxapi/SolidWorks.Interop.swbrowser~SolidWorks.Interop.swbrowser_namespace.html"
---

# SolidWorks.Interop.swbrowser Namespace

## Interfaces

| Interface | Description |
| --- | --- |
| IApplication | Provides access to the SOLIDWORKS Toolbox Browser add-in. |
| IPDMDocManager | Provides access to the SOLIDWORKS Toolbox document manager. |

## Delegates

| Delegate | Description |
| --- | --- |
| DApplicationEvents_DestroyEventHandler | Handles the notification that the Toolbox Browser is about to be destroyed. |
| DPDMDocManagerEvents_AfterCopyingDocumentEventHandler | Handles the notification that the specified PDM-managed document was copied to the specified new file name. |
| DPDMDocManagerEvents_AfterDeletingDocumentEventHandler | Handles the notification that the specified PDM-managed document was deleted. |
| DPDMDocManagerEvents_AfterWritingToDocumentEventHandler | Handles the notification that the specified PDM-managed document was written to. |
| DPDMDocManagerEvents_BeforeCopyingDocumentEventHandler | Handles the notification that the specified PDM-managed document is about to be copied to the specified new file name. |
| DPDMDocManagerEvents_BeforeDeletingDocumentEventHandler | Handles the notification that the specified PDM-managed document is about to be deleted. |
| DPDMDocManagerEvents_BeforeWritingToDocumentEventHandler | Handles the notification that the specified PDM-managed document is about to be written to. |
| DPDMDocManagerEvents_DestroyEventHandler | Handles the notification that the PDM application object is about to be destroyed. |
| DPDMDocManagerEvents_NewDocumentAddedEventHandler | Handles the notification that the specified part was added to the Toolbox. |
| DPDMDocManagerEvents_PreInsertDocumentEventHandler | Handles the notification that the specified PDM-managed document is about to be inserted into an assembly. |

## Enumerations

| Enumeration | Description |
| --- | --- |
| swApplicationEvents_e | Events to be handled by the SOLIDWORKS Toolbox Browser application. |
| swPDMDocManagerEvents_e | Events to be handled by the PDM application. |
| swPDMStatus_e | PDM document statuses. |

## See Also

[SolidWorks.Interop.swbrowser Assembly](SolidWorks.Interop.swbrowser.html)
