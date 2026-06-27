---
title: "eDrawings.Interop.EModelViewControl Namespace"
project: "eDrawings API Help"
interface: "eDrawings.Interop.EModelViewControl"
member: ""
kind: "namespace"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl_namespace.html"
---

# eDrawings.Interop.EModelViewControl Namespace

eDrawings API

## Interfaces

| Interface | Description |
| --- | --- |
| IEModelViewControl | Encapsulates the functionality of the eDrawings Viewer. |

## Delegates

| Delegate | Description |
| --- | --- |
| _IEModelViewControlEvents_OnAnimationsChangedEventHandler | Fired when an animation has changed. |
| _IEModelViewControlEvents_OnCameraChangeEventHandler | Fired when changing the camera, including changing a scene orbit and selecting a named view. |
| _IEModelViewControlEvents_OnCameraChangeFinishedEventHandler | Fired when changes to the camera have finished, including changing a scene orbit and selecting a named view. |
| _IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler | Fired when the cursor is over a component. |
| _IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler | Obsolete. Superseded by IEModelViewControlEvents::OnComponentMouseOverNotify2 |
| _IEModelViewControlEvents_OnComponentSelectionNotify2EventHandler | Fired when a component is selected. |
| _IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler | Obsolete. Superseded by IEModelViewControlEvent OnComponentSelectionNotify2 . |
| _IEModelViewControlEvents_OnConfigChangeEventHandler | Fired when the specified configuration changes. |
| _IEModelViewControlEvents_OnFailedLoadingDocumentEventHandler | Fired when the specified eDrawings document fails to load. |
| _IEModelViewControlEvents_OnFailedPrintingDocumentEventHandler | Fired if the printer name specified in the IEModelViewControl::SetPageSetupOptions was invalid or if an eDrawings-related error exists that prevents data from being sent to a printer queue. |
| _IEModelViewControlEvents_OnFailedSavingDocumentEventHandler | Fired when saving an eDrawings document fails. |
| _IEModelViewControlEvents_OnFinishedAnimationEventHandler | Fired when an animation has finished. |
| _IEModelViewControlEvents_OnFinishedLoadingDocumentEventHandler | Fired when the eDrawings file has finished loading. |
| _IEModelViewControlEvents_OnFinishedPrintingDocumentEventHandler | Fired when an eDrawings document finishes printing. |
| _IEModelViewControlEvents_OnFinishedSavingDocumentEventHandler | Fired when an eDrawings file finishes saving. |
| _IEModelViewControlEvents_OnModifySceneEventHandler | Fired when a scene is modified. |
| _IEModelViewControlEvents_OnNamedViewEventHandler | Fired when a named view has been selected. |
| _IEModelViewControlEvents_OnPrevNextPlayStartEventHandler | Fired when the animation starts when associated with the Preview , Next , or Play button. |
| _IEModelViewControlEvents_OnPrevNextPlayStopEventHandler | Fired when the animation stops when associated with the Preview , Next , or Play button. |
| _IEModelViewControlEvents_OnStartedAnimationEventHandler | Fired when an animation has started. |

## Enumerations

| Enumeration | Description |
| --- | --- |
| EMVAnimateAction | Animation actions. |
| EMVComponentState | Component states. Bitmask. |
| EMVEnableFeatures | Enable features. Bitmask. |
| EMVMassProperty | Mass properties. |
| EMVOperators | Select and view tools. |
| EMVPrintOrientation | Print orientations. |
| EMVPrintType | Print types. |
| EMVViewOrientation | View orientations. |
| EMVViewState | View states. Bitmask. |

## See Also

[eDrawings.Interop.EModelViewControl Assembly](eDrawings.Interop.EModelViewControl.html)
