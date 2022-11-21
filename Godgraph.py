import networkx as nx
import matplotlib.pyplot as plt

#Cria grafo vazio
G = nx.Graph()

#Adiciona Vértices
G.add_node('Chaos')
G.add_node('Erebus')
G.add_node('Nyx')
G.add_node('Charon')
G.add_node('Tartarus')
G.add_node('Gaia')
G.add_node('Ourea')
G.add_node('Typhone')
G.add_node('Echidna')
G.add_node('Orthrus')
G.add_node('Cerberus')
G.add_node('Colchian Dragon')
G.add_node('Chimera')
G.add_node('Hydra')
G.add_node('Sphinx')
G.add_node('Uranus')
G.add_node('Oceanus')
G.add_node('Tethys')
G.add_node('Hyperion')
G.add_node('Theia')
G.add_node('Crius')
G.add_node('Cronus')
G.add_node('Rhea')
G.add_node('Themis')
G.add_node('Iapetus')
G.add_node('Mnemosyne')
G.add_node('Coeus')
G.add_node('Phoebe')
G.add_node('Pontus')
G.add_node('Aether')
G.add_node('Hemera')
G.add_node('Thalassa')
G.add_node('Thaumus')
G.add_node('Iris')
G.add_node('Harpies')
G.add_node('Porcys')
G.add_node('Ceto')
G.add_node('Sirens')
G.add_node('Scylla')
G.add_node('Gorgons')
G.add_node('Graeae')
G.add_node('Eurybia')
G.add_node('Asia')
G.add_node('Nereus')
G.add_node('Doris')
G.add_node('Tyche')
G.add_node('Perse')
G.add_node('Eurynome')
G.add_node('Metis')
G.add_node('Styx')
G.add_node('Pleone')
G.add_node('Helios')
G.add_node('Selene')
G.add_node('Eos')
G.add_node('Astraeus')
G.add_node('Pallas')
G.add_node('Atlas')
G.add_node('Prometheus')
G.add_node('Epimetheus')
G.add_node('Pandora')
G.add_node('Amphitrite')
G.add_node('Poseidon')
G.add_node('Triton')
G.add_node('Demeter')
G.add_node('Zeus')
G.add_node('Hera')
G.add_node('Hades')
G.add_node('Hestia')
G.add_node('Maia')
G.add_node('Leto')
G.add_node('Asteria')
G.add_node('Athena')
G.add_node('Hebe')
G.add_node('Hephaestus')
G.add_node('Ares')
G.add_node('Aphrodite')
G.add_node('Adonis')
G.add_node('Hermes')
G.add_node('Apollo')
G.add_node('Artemis')

#Adiciona Arestas
G.add_edge('Chaos', 'Erebus')
G.add_edge('Gorgons', 'Graeae')
G.add_edge('Eurybia', 'Astraeus')
G.add_edge('Eurybia', 'Pallas')
G.add_edge('Asia', 'Doris')
G.add_edge('Asia', 'Tyche')
G.add_edge('Asia', 'Perse')
G.add_edge('Asia', 'Eurynome')
G.add_edge('Asia', 'Metis')
G.add_edge('Asia', 'Styx')
G.add_edge('Asia', 'Pleone')
G.add_edge('Nereus', 'Doris')
G.add_edge('Nereus', 'Amphitrite')
G.add_edge('Nereus', 'Thetis')
G.add_edge('Doris', 'Tyche')
G.add_edge('Doris', 'Perse')
G.add_edge('Doris', 'Eurynome')
G.add_edge('Doris', 'Metis')
G.add_edge('Doris', 'Styx')
G.add_edge('Doris', 'Pleone')
G.add_edge('Doris', 'Amphitrite')
G.add_edge('Doris', 'Thetis')
G.add_edge('Tyche', 'Perse')
G.add_edge('Tyche', 'Eurynome')
G.add_edge('Tyche', 'Metis')
G.add_edge('Tyche', 'Styx')
G.add_edge('Tyche', 'Pleone')
G.add_edge('Perse', 'Eurynome')
G.add_edge('Perse', 'Metis')
G.add_edge('Perse', 'Styx')
G.add_edge('Perse', 'Pleone')
G.add_edge('Perse', 'Helios')
G.add_edge('Eurynome', 'Metis')
G.add_edge('Eurynome', 'Styx')
G.add_edge('Eurynome', 'Pleone')
G.add_edge('Eurynome', 'Zeus')
G.add_edge('Metis', 'Styx')
G.add_edge('Metis', 'Pleone')
G.add_edge('Metis', 'Zeus')
G.add_edge('Metis', 'Athena')
G.add_edge('Styx', 'Pleone')
G.add_edge('Styx', 'Pallas')
G.add_edge('Pleone', 'Atlas')
G.add_edge('Pleone', 'Maia')
G.add_edge('Helios', 'Selene')
G.add_edge('Helios', 'Eos')
G.add_edge('Selene', 'Eos')
G.add_edge('Eos', 'Astraeus')
G.add_edge('Astraeus', 'Pallas')
G.add_edge('Atlas', 'Prometheus')
G.add_edge('Atlas', 'Epimetheus')
G.add_edge('Atlas', 'Maia')
G.add_edge('Prometheus', 'Epimetheus')
G.add_edge('Epimetheus', 'Pandora')
G.add_edge('Amphitrite', 'Poseidon')
G.add_edge('Amphitrite', 'Triton')
G.add_edge('Poseidon', 'Triton')
G.add_edge('Poseidon', 'Demeter')
G.add_edge('Poseidon', 'Zeus')
G.add_edge('Poseidon', 'Hera')
G.add_edge('Poseidon', 'Hades')
G.add_edge('Poseidon', 'Hestia')
G.add_edge('Demeter', 'Zeus')
G.add_edge('Demeter', 'Hera')
G.add_edge('Demeter', 'Hades')
G.add_edge('Demeter', 'Hestia')
G.add_edge('Zeus', 'Hera')
G.add_edge('Zeus', 'Hades')
G.add_edge('Zeus', 'Hestia')
G.add_edge('Zeus', 'Hephaestus')
G.add_edge('Zeus', 'Ares')
G.add_edge('Zeus', 'Apollo')
G.add_edge('Zeus', 'Artemis')
G.add_edge('Zeus', 'Maia')
G.add_edge('Zeus', 'Hebe')
G.add_edge('Zeus', 'Leto')
G.add_edge('Zeus', 'Athena')
G.add_edge('Hera', 'Hebe')
G.add_edge('Hera', 'Hephaestus')
G.add_edge('Hera', 'Ares')
G.add_edge('Hera', 'Hades')
G.add_edge('Hera', 'Hestia')
G.add_edge('Hades', 'Hestia')
G.add_edge('Maia', 'Hermes')
G.add_edge('Leto', 'Apollo')
G.add_edge('Leto', 'Artemis')
G.add_edge('Leto', 'Asteria')
G.add_edge('Hebe', 'Hephaestus')
G.add_edge('Hebe', 'Ares')
G.add_edge('Hephaestus', 'Ares')
G.add_edge('Aphrodite', 'Adonis')
G.add_edge('Apollo', 'Artemis')
G.add_edge('Chaos', 'Tartarus')
G.add_edge('Chaos', 'Gaia')
G.add_edge('Chaos', 'Nyx')
G.add_edge('Erebus', 'Tartarus')
G.add_edge('Erebus', 'Gaia')
G.add_edge('Erebus', 'Nyx')
G.add_edge('Erebus', 'Aether')
G.add_edge('Erebus', 'Hemera')
G.add_edge('Erebus', 'Charon')
G.add_edge('Nyx', 'Tartarus')
G.add_edge('Nyx', 'Gaia')
G.add_edge('Nyx', 'Aether')
G.add_edge('Nyx', 'Hemera')
G.add_edge('Nyx', 'Charon')
G.add_edge('Tartarus', 'Gaia')
G.add_edge('Tartarus', 'Typhone')
G.add_edge('Tartarus', 'Echidna')
G.add_edge('Gaia', 'Ourea')
G.add_edge('Gaia', 'Uranus')
G.add_edge('Gaia', 'Pontus')
G.add_edge('Gaia', 'Typhone')
G.add_edge('Gaia', 'Echidna')
G.add_edge('Gaia', 'Thaumus')
G.add_edge('Gaia', 'Porcys')
G.add_edge('Gaia', 'Ceto')
G.add_edge('Gaia', 'Eurybia')
G.add_edge('Gaia', 'Nereus')
G.add_edge('Gaia', 'Oceanus')
G.add_edge('Gaia', 'Tethys')
G.add_edge('Gaia', 'Hyperion')
G.add_edge('Gaia', 'Theia')
G.add_edge('Gaia', 'Crius')
G.add_edge('Gaia', 'Rhea')
G.add_edge('Gaia', 'Themis')
G.add_edge('Gaia', 'Iapetus')
G.add_edge('Gaia', 'Mnemosyne')
G.add_edge('Gaia', 'Coeus')
G.add_edge('Gaia', 'Phoebe')
G.add_edge('Gaia', 'Cronus')
G.add_edge('Typhone', 'Echidna')
G.add_edge('Typhone', 'Orthrus')
G.add_edge('Typhone', 'Cerberus')
G.add_edge('Typhone', 'Colchian Dragon')
G.add_edge('Typhone', 'Chimera')
G.add_edge('Typhone', 'Hydra')
G.add_edge('Typhone', 'Sphinx')
G.add_edge('Echidna', 'Orthrus')
G.add_edge('Echidna', 'Cerberus')
G.add_edge('Echidna', 'Colchian Dragon')
G.add_edge('Echidna', 'Chimera')
G.add_edge('Echidna', 'Hydra')
G.add_edge('Echidna', 'Sphinx')
G.add_edge('Orthrus', 'Cerberus')
G.add_edge('Orthrus', 'Colchian Dragon')
G.add_edge('Orthrus', 'Chimera')
G.add_edge('Orthrus', 'Hydra')
G.add_edge('Orthrus', 'Sphinx')
G.add_edge('Cerberus', 'Colchian Dragon')
G.add_edge('Cerberus', 'Chimera')
G.add_edge('Cerberus', 'Hydra')
G.add_edge('Cerberus', 'Sphinx')
G.add_edge('Colchian Dragon', 'Chimera')
G.add_edge('Colchian Dragon', 'Hydra')
G.add_edge('Colchian Dragon', 'Sphinx')
G.add_edge('Chimera', 'Hydra')
G.add_edge('Chimera', 'Sphinx')
G.add_edge('Hydra', 'Sphinx')
G.add_edge('Uranus', 'Oceanus')
G.add_edge('Uranus', 'Tethys')
G.add_edge('Uranus', 'Hyperion')
G.add_edge('Uranus', 'Theia')
G.add_edge('Uranus', 'Crius')
G.add_edge('Uranus', 'Cronus')
G.add_edge('Uranus', 'Rhea')
G.add_edge('Uranus', 'Themis')
G.add_edge('Uranus', 'Iapetus')
G.add_edge('Uranus', 'Mnemosyne')
G.add_edge('Uranus', 'Coeus')
G.add_edge('Uranus', 'Phoebe')
G.add_edge('Uranus', 'Aphrodite')
G.add_edge('Oceanus', 'Tethys')
G.add_edge('Oceanus', 'Hyperion')
G.add_edge('Oceanus', 'Theia')
G.add_edge('Oceanus', 'Crius')
G.add_edge('Oceanus', 'Cronus')
G.add_edge('Oceanus', 'Rhea')
G.add_edge('Oceanus', 'Themis')
G.add_edge('Oceanus', 'Iapetus')
G.add_edge('Oceanus', 'Mnemosyne')
G.add_edge('Oceanus', 'Coeus')
G.add_edge('Oceanus', 'Phoebe')
G.add_edge('Oceanus', 'Doris')
G.add_edge('Oceanus', 'Tyche')
G.add_edge('Oceanus', 'Perse')
G.add_edge('Oceanus', 'Eurynome')
G.add_edge('Oceanus', 'Metis')
G.add_edge('Oceanus', 'Styx')
G.add_edge('Oceanus', 'Pleone')
G.add_edge('Oceanus', 'Asia')
G.add_edge('Tethys', 'Hyperion')
G.add_edge('Tethys', 'Theia')
G.add_edge('Tethys', 'Crius')
G.add_edge('Tethys', 'Cronus')
G.add_edge('Tethys', 'Rhea')
G.add_edge('Tethys', 'Themis')
G.add_edge('Tethys', 'Iapetus')
G.add_edge('Tethys', 'Mnemosyne')
G.add_edge('Tethys', 'Coeus')
G.add_edge('Tethys', 'Phoebe')
G.add_edge('Tethys', 'Doris')
G.add_edge('Tethys', 'Tyche')
G.add_edge('Tethys', 'Perse')
G.add_edge('Tethys', 'Eurynome')
G.add_edge('Tethys', 'Metis')
G.add_edge('Tethys', 'Styx')
G.add_edge('Tethys', 'Pleone')
G.add_edge('Tethys', 'Asia')
G.add_edge('Hyperion', 'Theia')
G.add_edge('Hyperion', 'Crius')
G.add_edge('Hyperion', 'Cronus')
G.add_edge('Hyperion', 'Rhea')
G.add_edge('Hyperion', 'Themis')
G.add_edge('Hyperion', 'Iapetus')
G.add_edge('Hyperion', 'Mnemosyne')
G.add_edge('Hyperion', 'Coeus')
G.add_edge('Hyperion', 'Phoebe')
G.add_edge('Hyperion', 'Helios')
G.add_edge('Hyperion', 'Selene')
G.add_edge('Hyperion', 'Eos')
G.add_edge('Theia', 'Crius')
G.add_edge('Theia', 'Cronus')
G.add_edge('Theia', 'Rhea')
G.add_edge('Theia', 'Themis')
G.add_edge('Theia', 'Iapetus')
G.add_edge('Theia', 'Mnemosyne')
G.add_edge('Theia', 'Coeus')
G.add_edge('Theia', 'Phoebe')
G.add_edge('Theia', 'Helios')
G.add_edge('Theia', 'Selene')
G.add_edge('Theia', 'Eos')
G.add_edge('Crius', 'Cronus')
G.add_edge('Crius', 'Rhea')
G.add_edge('Crius', 'Themis')
G.add_edge('Crius', 'Iapetus')
G.add_edge('Crius', 'Mnemosyne')
G.add_edge('Crius', 'Coeus')
G.add_edge('Crius', 'Phoebe')
G.add_edge('Crius', 'Eurybia')
G.add_edge('Cronus', 'Rhea')
G.add_edge('Cronus', 'Themis')
G.add_edge('Cronus', 'Iapetus')
G.add_edge('Cronus', 'Mnemosyne')
G.add_edge('Cronus', 'Coeus')
G.add_edge('Cronus', 'Phoebe')
G.add_edge('Cronus', 'Poseidon')
G.add_edge('Cronus', 'Demeter')
G.add_edge('Cronus', 'Zeus')
G.add_edge('Cronus', 'Hera')
G.add_edge('Cronus', 'Hades')
G.add_edge('Cronus', 'Hestia')
G.add_edge('Rhea', 'Themis')
G.add_edge('Rhea', 'Iapetus')
G.add_edge('Rhea', 'Mnemosyne')
G.add_edge('Rhea', 'Coeus')
G.add_edge('Rhea', 'Phoebe')
G.add_edge('Rhea', 'Poseidon')
G.add_edge('Rhea', 'Demeter')
G.add_edge('Rhea', 'Zeus')
G.add_edge('Rhea', 'Hera')
G.add_edge('Rhea', 'Hades')
G.add_edge('Rhea', 'Hestia')
G.add_edge('Themis', 'Iapetus')
G.add_edge('Themis', 'Mnemosyne')
G.add_edge('Themis', 'Coeus')
G.add_edge('Themis', 'Phoebe')
G.add_edge('Themis', 'Zeus')
G.add_edge('Iapetus', 'Mnemosyne')
G.add_edge('Iapetus', 'Coeus')
G.add_edge('Iapetus', 'Phoebe')
G.add_edge('Iapetus', 'Asia')
G.add_edge('Iapetus', 'Atlas')
G.add_edge('Iapetus', 'Prometheus')
G.add_edge('Iapetus', 'Epimetheus')
G.add_edge('Mnemosyne', 'Coeus')
G.add_edge('Mnemosyne', 'Phoebe')
G.add_edge('Mnemosyne', 'Zeus')
G.add_edge('Mnemosyne', 'Muses')
G.add_edge('Coeus', 'Phoebe')
G.add_edge('Coeus', 'Leto')
G.add_edge('Coeus', 'Asteria')
G.add_edge('Phoebe', 'Leto')
G.add_edge('Phoebe', 'Asteria')
G.add_edge('Pontus', 'Thalassa')
G.add_edge('Pontus', 'Thaumus')
G.add_edge('Pontus', 'Porcys')
G.add_edge('Pontus', 'Ceto')
G.add_edge('Pontus', 'Eurybia')
G.add_edge('Pontus', 'Mereus')
G.add_edge('Aether', 'Hemera')
G.add_edge('Aether', 'Thalassa')
G.add_edge('Hemera', 'Thalassa')
G.add_edge('Thaumus', 'Iris')
G.add_edge('Thaumus', 'Harpies')
G.add_edge('Iris', 'Harpies')
G.add_edge('Porcys', 'Ceto')
G.add_edge('Porcys', 'Sirens')
G.add_edge('Porcys', 'Scylla')
G.add_edge('Porcys', 'Gorgons')
G.add_edge('Porcys', 'Graeae')
G.add_edge('Ceto', 'Sirens')
G.add_edge('Ceto', 'Scylla')
G.add_edge('Ceto', 'Gorgons')
G.add_edge('Ceto', 'Graeae')
G.add_edge('Sirens', 'Scylla')
G.add_edge('Sirens', 'Gorgons')
G.add_edge('Sirens', 'Graeae')
G.add_edge('Scylla', 'Gorgons')
G.add_edge('Scylla', 'Graeae')

print('Plotando grafo como imagem. Verifique o arquivo graph.png.')
f = plt.figure(1)
f.set_figwidth(60)
f.set_figheight(60)
nx.draw_networkx(G, pos=nx.spring_layout(G), with_labels=True)
plt.savefig('graph.png')