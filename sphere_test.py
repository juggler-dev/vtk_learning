##Notes:

# # vtkSphereSource: Generates the geometry of a sphere.
# # vtkPolyDataMapper: Maps the geometry into a form that VTK can render.
# # vtkActor: Represents the object in the scene.
# # vtkRenderer: Manages how objects are drawn.
# # vtkRenderWindow: A window for rendering.
# # vtkRenderWindowInteractor: Allows user interaction (e.g., zooming, rotating).

import vtk

# Create a sphere source
sphere_source = vtk.vtkSphereSource()
sphere_source.SetRadius(5.0)
sphere_source.SetThetaResolution(50)
sphere_source.SetPhiResolution(50)

# Create a mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere_source.GetOutputPort())

# Create an actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetColor(0.1, 0.5, 0.8)  # Set color (R, G, B)

# Create a renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0.2, 0.2, 0.2)  # Set background color

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)
render_window.SetSize(600, 600)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the rendering loop
render_window.Render()
interactor.Start()
